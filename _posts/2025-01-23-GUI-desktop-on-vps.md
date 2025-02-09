<div contenteditable="true">
  <hr>
  </div>
  <h2>
    <span>layout: post title: GUI remote desktop date: 2025-01-23 00:00:00 +0300 img: hello-world.jpg # Add image post (optional) tags: [GUI, ssh, remote, xfce] # add tag</span>
  </h2>
  <h1>
    <span>🖥️ HOW CAN YOU HAVE A DESKTOP REMOTE ENVIRONMENT</span>
  </h1>
  <p>
    <span>
      <em>(Focuses on XFCE4 / XFCE4-session for some xstartup commands.)</em>
    </span>
  </p>
  <h2>
    <span>🔧 Step 1: Update and Install Required Packages</span>
  </h2>
  <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ61" data-is-code-block-view="true" contenteditable="false">
    <div class="cm-announced" aria-live="polite"></div>
    <div tabindex="-1" class="cm-scroller">
      <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
        <div class="cm-line">apt update &amp;&amp; apt upgrade 
          <span class="ͼ2u">-y</span>
        </div>
        <div class="cm-line">apt install 
          <span class="ͼ2u">-y</span> xfce4 xfce4-goodies tigervnc-standalone-server 
          <span class="ͼ2u">wget</span>
          <span class="ͼ2u">curl</span>
          <span class="ͼ2u">git</span> dbus-x11
        </div>
      </div>
      <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms; transform: scale(1, 1);">
        <div class="cm-cursor cm-cursor-primary" style="left: 6px; top: 5.59998px; height: 18.4px;"></div>
      </div>
      <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2; transform: scale(1, 1);"></div>
    </div>
  </div>
  <h2>
    <span>🔑 Step 2: Create a VNC Password for the Server</span>
  </h2>
  <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ62" data-is-code-block-view="true" contenteditable="false">
    <div class="cm-announced" aria-live="polite"></div>
    <div tabindex="-1" class="cm-scroller">
      <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
        <div class="cm-line">vncpasswd</div>
      </div>
      <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms; transform: scale(1, 1);">
        <div class="cm-cursor cm-cursor-primary" style="left: 6px; top: 5.60004px; height: 18.4px;"></div>
      </div>
      <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2; transform: scale(1, 1);"></div>
    </div>
  </div>
  <h2>
    <span>📥 Step 3: Clone the noVNC Repository</span>
  </h2>
  <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ63" data-is-code-block-view="true" contenteditable="false">
    <div class="cm-announced" aria-live="polite"></div>
    <div tabindex="-1" class="cm-scroller">
      <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
        <div class="cm-line">
          <span class="ͼ2u">git</span> clone https://github.com/novnc/noVNC.git /opt/novnc
        </div>
      </div>
      <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
        <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
      </div>
      <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
    </div>
  </div>
  <h2>
    <span>📂 Step 4: Navigate to the noVNC Directory</span>
  </h2>
  <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ64" data-is-code-block-view="true" contenteditable="false">
    <div class="cm-announced" aria-live="polite"></div>
    <div tabindex="-1" class="cm-scroller">
      <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
        <div class="cm-line">
          <span class="ͼ2u">cd</span> /opt/novnc/utils
        </div>
        <div class="cm-line">
          <span class="ͼ2u">ln</span>
          <span class="ͼ2u">-s</span> ../novnc_proxy .
        </div>
      </div>
      <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
        <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48798px; height: 18.032px;"></div>
      </div>
      <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
    </div>
  </div>
  <h2>
    <span>🚀 Step 5: Run noVNC</span>
  </h2>
  <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ65" data-is-code-block-view="true" contenteditable="false">
    <div class="cm-announced" aria-live="polite"></div>
    <div tabindex="-1" class="cm-scroller">
      <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
        <div class="cm-line">/opt/novnc/utils/novnc_proxy 
          <span class="ͼ2u">--vnc</span> localhost:5901
        </div>
      </div>
      <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
        <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
      </div>
      <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
    </div>
  </div>
  <div contenteditable="false">
    <hr>
    </div>
    <h2>
      <span>🏆 Preferred Way (xstartup)</span>
    </h2>
    <h3>
      <span>✅ Confirm Desktop is Enabled</span>
    </h3>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ66" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ2s ͼb">export</span>
            <span class="ͼ2u ͼg">DISPLAY</span>
            <span class="ͼ2z">=</span>:1
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <p>
      <span>Check with:</span>
    </p>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ67" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ2u">echo</span>
            <span class="ͼ2u ͼg">$DISPLAY</span>
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48792px; height: 18.0321px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <h3>
      <span>📂 Navigate to </span>
      <code>
        <span>.vnc</span>
      </code>
      <span> Folder</span>
    </h3>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ68" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ2u">ls</span>
            <span class="ͼ2u">-la</span>
          </div>
          <div class="cm-line">
            <span class="ͼ2u">cd</span> .vnc
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <h3>
      <span>📝 Create xstartup File</span>
    </h3>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ69" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">nano xstartup</div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <p>
      <span>📜 </span>
      <span>
        <strong>Content of </strong>
      </span>
      <span>
        <strong>
          <strong>
            <strong>``</strong>
          </strong>
        </strong>
      </span>
      <span>
        <strong> for a VNCServer with XFCE Desktop:</strong>
      </span>
    </p>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6a" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ36 ͼ5">#!/bin/sh</span>
          </div>
          <div class="cm-line">
            <span class="ͼ2s ͼb">unset</span> SESSION_MANAGER
          </div>
          <div class="cm-line">
            <span class="ͼ2s ͼb">unset</span> DBUS_SESSION_BUS_ADDRESS
          </div>
          <div class="cm-line">/usr/bin/startxfce4</div>
          <div class="cm-line">[ 
            <span class="ͼ2u">-x</span> /etc/vnc/xstartup ] &amp;&amp; exec /etc/vnc/xstartup
          </div>
          <div class="cm-line">x-window-manager &amp;</div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <h3>
      <span>🔧 Set Executable Permissions</span>
    </h3>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6b" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ2u">chmod</span>
            <span class="ͼ2z">+</span>x /root/.vnc/xstartup
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <p>
      <span>(Optional):</span>
    </p>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6c" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">
            <span class="ͼ2u">chown</span> root:root /root/.vnc/xstartup
          </div>
          <div class="cm-line">
            <span class="ͼ2u">chmod</span>
            <span class="ͼ2y ͼd">755</span> /root/.vnc/xstartup
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <h3>
      <span>🚀 Start VNC Server</span>
    </h3>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6d" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">vncserver :1</div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0317px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <p>
      <span>To kill VNC Server:</span>
    </p>
    <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6e" data-is-code-block-view="true" contenteditable="false">
      <div class="cm-announced" aria-live="polite"></div>
      <div tabindex="-1" class="cm-scroller">
        <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
          <div class="cm-line">vncserver 
            <span class="ͼ2u">-kill</span> :1
          </div>
        </div>
        <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
          <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.0317px;"></div>
        </div>
        <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
      </div>
    </div>
    <p>
      <span>🔗 </span>
      <span>
        <strong>Open port </strong>
      </span>
      <span>
        <strong>
          <strong>
            <strong>``</strong>
          </strong>
        </strong>
      </span>
      <span>
        <strong> (or the assigned one) in your browser and enjoy!</strong>
      </span>
    </p>
    <div contenteditable="false">
      <hr>
      </div>
      <h2>
        <span>🔄 Alternative Ways</span>
      </h2>
      <h3>
        <span>⚡ If </span>
        <code>
          <span>vncserver :1</span>
        </code>
        <span> Gives Errors:</span>
      </h3>
      <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6f" data-is-code-block-view="true" contenteditable="false">
        <div class="cm-announced" aria-live="polite"></div>
        <div tabindex="-1" class="cm-scroller">
          <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
            <div class="cm-line">tigervncserver 
              <span class="ͼ2u">-xstartup</span> /usr/bin/xterm
            </div>
          </div>
          <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
            <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
          </div>
          <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
        </div>
      </div>
      <p>
        <span>Then in the noVNC virtual terminal:</span>
      </p>
      <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6g" data-is-code-block-view="true" contenteditable="false">
        <div class="cm-announced" aria-live="polite"></div>
        <div tabindex="-1" class="cm-scroller">
          <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
            <div class="cm-line">xfce4-session 
              <span class="ͼ2u">--display</span>
              <span class="ͼ2z">=</span>:1
            </div>
          </div>
          <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
            <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.032px;"></div>
          </div>
          <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
        </div>
      </div>
      <h3>
        <span>🖥️ Running Apps Without Full Desktop</span>
      </h3>
      <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6h" data-is-code-block-view="true" contenteditable="false">
        <div class="cm-announced" aria-live="polite"></div>
        <div tabindex="-1" class="cm-scroller">
          <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
            <div class="cm-line">apt install 
              <span class="ͼ2u">-y</span> x11-apps
            </div>
            <div class="cm-line">xclock</div>
          </div>
          <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
            <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0317px;"></div>
          </div>
          <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
        </div>
      </div>
      <h3>
        <span>❌ Without Using </span>
        <code>
          <span>xstartup</span>
        </code>
      </h3>
      <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6i" data-is-code-block-view="true" contenteditable="false">
        <div class="cm-announced" aria-live="polite"></div>
        <div tabindex="-1" class="cm-scroller">
          <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
            <div class="cm-line">vncserver :1</div>
            <div class="cm-line">xfce4-session 
              <span class="ͼ2u">--display</span>
              <span class="ͼ2z">=</span>:1
            </div>
          </div>
          <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
            <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.0322px;"></div>
          </div>
          <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
        </div>
      </div>
      <p>
        <span>To stop XFCE4:</span>
      </p>
      <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6j" data-is-code-block-view="true" contenteditable="false">
        <div class="cm-announced" aria-live="polite"></div>
        <div tabindex="-1" class="cm-scroller">
          <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
            <div class="cm-line">xfce4-session-logout 
              <span class="ͼ2u">--logout</span>
            </div>
          </div>
          <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
            <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
          </div>
          <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
        </div>
      </div>
      <div contenteditable="false">
        <hr>
        </div>
        <h2>
          <span>🔥 HOT: Use SSH with X11 Forwarding (For GUI Apps)</span>
        </h2>
        <p>
          <span>Run GUI Apps from the Container:</span>
        </p>
        <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6k" data-is-code-block-view="true" contenteditable="false">
          <div class="cm-announced" aria-live="polite"></div>
          <div tabindex="-1" class="cm-scroller">
            <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
              <div class="cm-line">apt install 
                <span class="ͼ2u">-y</span> openssh-server
              </div>
              <div class="cm-line">
                <span class="ͼ2u">ssh</span>
                <span class="ͼ2u">-X</span> user@localhost 
                <span class="ͼ2u">-p</span>
                <span class="ͼ2y ͼd">2222</span>
              </div>
            </div>
            <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
              <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
            </div>
            <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
          </div>
        </div>
        <p>
          <span>
            <em>(Modify accordingly 😎.)</em>
          </span>
        </p>
        <div contenteditable="false">
          <hr>
          </div>
          <h2>
            <span>🛠️ TIPS: Use </span>
            <code>
              <span>-geometry</span>
            </code>
            <span> for Resolution Adjustment</span>
          </h2>
          <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6l" data-is-code-block-view="true" contenteditable="false">
            <div class="cm-announced" aria-live="polite"></div>
            <div tabindex="-1" class="cm-scroller">
              <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
                <div class="cm-line">vncserver :1 
                  <span class="ͼ2u">-geometry</span> 1535x824
                </div>
              </div>
              <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
                <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.0322px;"></div>
              </div>
              <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
            </div>
          </div>
          <p>
            <span>
              <em>(For my laptop.)</em>
            </span>
          </p>
          <div contenteditable="false">
            <hr>
            </div>
            <h2>
              <span>🌐 Inside GUI Desktop: Installing a Browser</span>
            </h2>
            <p>
              <span>To install </span>
              <span>
                <strong>Falkon</strong>
              </span>
              <span>:</span>
            </p>
            <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6m" data-is-code-block-view="true" contenteditable="false">
              <div class="cm-announced" aria-live="polite"></div>
              <div tabindex="-1" class="cm-scroller">
                <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
                  <div class="cm-line">apt install falkon</div>
                </div>
                <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
                  <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.032px;"></div>
                </div>
                <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
              </div>
            </div>
            <p>
              <span>🔹 </span>
              <span>
                <strong>Fixing Browser Launch Issues:</strong>
              </span>
            </p>
            <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6n" data-is-code-block-view="true" contenteditable="false">
              <div class="cm-announced" aria-live="polite"></div>
              <div tabindex="-1" class="cm-scroller">
                <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
                  <div class="cm-line">
                    <span class="ͼ2u">cd</span> /usr/bin/
                  </div>
                  <div class="cm-line">
                    <span class="ͼ2u">sudo</span> env 
                    <span class="ͼ2u ͼg">QTWEBENGINE_DISABLE_SANDBOX</span>
                    <span class="ͼ2z">=</span>
                    <span class="ͼ2y ͼd">1</span> ./MyApp
                  </div>
                </div>
                <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
                  <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.0315px;"></div>
                </div>
                <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
              </div>
            </div>
            <p>
              <span>
                <em>(Replace </em>
              </span>
              <code>
                <span>
                  <strong>
                    <em>** with **</em>
                  </strong>
                </span>
              </code>
              <span>
                <em> or any other browser.)</em>
              </span>
            </p>
            <h3>
              <span>🆕 Alternative: Creating a Sub-User</span>
            </h3>
            <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6o" data-is-code-block-view="true" contenteditable="false">
              <div class="cm-announced" aria-live="polite"></div>
              <div tabindex="-1" class="cm-scroller">
                <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
                  <div class="cm-line">
                    <span class="ͼ2u">sudo</span> adduser newuser_name
                  </div>
                </div>
                <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
                  <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.032px;"></div>
                </div>
                <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
              </div>
            </div>
            <p>
              <span>Then test with:</span>
            </p>
            <div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6p" data-is-code-block-view="true" contenteditable="false">
              <div class="cm-announced" aria-live="polite"></div>
              <div tabindex="-1" class="cm-scroller">
                <div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
                  <div class="cm-line">./MyApp 
                    <span class="ͼ2u">--no</span>
                    <span class="ͼ2u">-sandbox</span>
                  </div>
                </div>
                <div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
                  <div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
                </div>
                <div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
              </div>
            </div>
            <p>
              <span>🚀 </span>
              <span>
                <strong>Enjoy Your Remote GUI Desktop!</strong>
              </span>
            </p>
            <p>
              <br class="ProseMirror-trailingBreak">
              </p>
</div>
            
