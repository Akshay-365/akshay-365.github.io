import gradio as gr
from ping_scheduler import manual_ping, get_ping_log, get_missed_pongs, last_ping
from pong_bot import get_pong_log, get_last_pong

# Limit the number of logs to display
MAX_LOG_ENTRIES = 20

def get_logs():
    pings = get_ping_log()[-MAX_LOG_ENTRIES:]  # Keep last N entries
    pongs = get_pong_log()[-MAX_LOG_ENTRIES:]
    missed = get_missed_pongs()

    log_text = "🟢 **Pings**:\n"
    log_text += "\n".join(f"- {t[1]}" for t in pings) if pings else "- None"

    log_text += "\n\n🔵 **Pongs**:\n"
    log_text += "\n".join(f"- {t[1]}" for t in pongs) if pongs else "- None"

    log_text += "\n\n⚠️ **Missed Pongs** (last 5):\n"
    log_text += "\n".join(f"- {m}" for m in missed[-5:]) if missed else "- None 🎉"

    log_text += "\n\n📈 **Last Ping**: " + (last_ping.strftime("%H:%M:%S") if last_ping else "None")
    log_text += "\n📈 **Last Pong**: " + get_last_pong()

    return log_text

# ✅ Support URL-triggered ping via ?ping=true
def on_load(request: gr.Request):
    query = getattr(request, "query_params", {})
    print("🔥 Incoming request with query:", dict(query))

    if query.get("ping", "false").lower() == "true":
        return manual_ping()
    return get_logs()

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Telegram Ping Pong Monitor with Watchdog")

    with gr.Row():
        refresh_btn = gr.Button("🔁 Refresh Logs")
        ping_btn = gr.Button("📤 Send Ping Now")

    output = gr.Textbox(lines=20, interactive=False, label="Ping-Pong Logs + Watchdog")

    # Button actions
    refresh_btn.click(get_logs, outputs=output)
    ping_btn.click(manual_ping, outputs=output)

    # ✅ Load handler (triggers ping if ?ping=true, else shows logs)
    demo.load(fn=on_load, inputs=None, outputs=output)

def launch_ui():
    # Share=True ensures public link; enable API for external tools
    demo.launch()


########################## -------  CODE FROM "main.py" --------###############################

import threading
from ping_scheduler import start_ping_loop
from pong_bot import run_pong_bot
# from gradio_interface import launch_ui

if __name__ == "__main__":
    threading.Thread(target=start_ping_loop, daemon=True).start()
    threading.Thread(target=run_pong_bot, daemon=True).start()
    launch_ui()
