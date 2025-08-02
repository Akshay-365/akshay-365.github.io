---
layout: post
title: One-Click Screenshot to AI- My Extension Mod 
date: 2025-08-02 00:00:00 +0300
description: A breakdown of how I modified the "GoFullPage" Chrome extension using JavaScript. This tutorial covers adding new UI elements, handling image data, and injecting scripts to automate uploading a screenshot to a third-party web application like Google AI Studio.
tags: [JavaScript, ChromeExtension, GenerativeAI, Automation] # add tag
---

# My Journey: Hacking a Chrome Extension to Automate a GenAI Course 🚀

This story begins with a simple goal during my Tata micro-internship on Generative AI 🎓. I wanted to find a clever way to automate the course, not by skipping videos, but by using the course material itself—specifically, the images and screenshots—as input for an AI.

### The Spark of an Idea 💡

My plan was to take full-page screenshots of the course content and feed them to a powerful AI model to summarize, analyze, or even answer questions. This felt like a practical and exciting way to apply the concepts I was learning.

### Assembling the Toolkit 🛠️

To bring this idea to life, I chose a few key tools:

*   **The AI Brain:** **Google's AI Studio (Gemini)**. It's fantastic for multimodal tasks, including understanding images.
*   **The Screenshot Tool:** I needed a reliable way to capture full web pages. After a quick search, I settled on a popular Chrome extension: **"GoFullPage - Full Page Screen Capture."**

### Hitting a Wall 🚧

The plan seemed solid until I hit a roadblock. The GoFullPage extension was excellent at taking screenshots, but it had no built-in feature to directly upload or send the captured image to an AI platform like Google's AI Studio. Manually saving each image and then uploading it would defeat the whole purpose of automation.

### The "I'll Do It Myself" Moment 👨‍💻

Instead of giving up, I decided to build the feature myself. Chrome extensions are just a collection of HTML, CSS, and JavaScript files. So, I thought, why not modify the existing extension to add the functionality I needed?

I downloaded the source code of the GoFullPage extension, rolled up my sleeves, and started modifying its files to create my own AI-enhanced version.

### The Grand Reveal: It Works! 🎉

After some trial, error, and a lot of fun, I successfully integrated the "Send to AI Studio" functionality directly into the extension's interface! Now, with a single click, I can send a full-page screenshot straight to Gemini.

---

### Peek Under the Hood: Explore the Code 🔍

For those who want to dive into the technical details, I've packaged everything for you. You can explore the original code, my modified version, and see a detailed analysis of every single change I made.

*   **🤖 My AI-Extended Version:** [**Download AI-Extended Version.zip**][ai-zip]
*   **📄 Original GoFullPage Version:** [**Download Original Version.zip**][original-zip]

[ai-zip]: /assets/img/extension-mod/8.5_0%20-%20extended%20by%20me.zip
[original-zip]: /assets/img/extension-mod/8.5_0%20-%20original.zip

For your convenience, here are the diff analyses that break down the changes:

*   **📊 Directory Comparison Overview:** [Click for PDF](/assets/img/extension-mod/changes.pdf)
*   **🔬 Deep Diff Analysis:** [View as PDF](/assets/img/extension-mod/diffscope.pdf)

### 📊 Directory Comparison Overview

<iframe src="/assets/img/extension-mod/changes.pdf" width="100%" height="600px" style="border:1px solid #ddd;">
   <p>Your browser does not support PDFs. <a href="/assets/img/extension-mod/changes.pdf">Download the PDF</a>.</p>
</iframe>

### 🔬 Deep Diff Analysis

For a complete line-by-line comparison, explore the interactive diff report embedded below. This shows every single code change between the original and my modified version.

<iframe src="/assets/img/extension-mod/index.html" width="100%" height="800px" style="border:1px solid #ddd; background: #fff;">
   <p>Your browser does not support iframes. <a href="/assets/img/extension-mod/index.html">View the interactive diff analysis</a>.</p>
</iframe>

---

### Technical Deep Dive: What Exactly Did I Change? 🔬

Based on the diff analysis, here’s a summary of the key modifications I made to bring this feature to life.

#### 1. `manifest.json` (The Extension's Blueprint)
This is the most critical file. I had to declare new permissions and features:
*   **Added a New Button:** A shiny "Send to AI Studio" button is now part of the UI.
*   **Host Permissions:** Granted the extension permission to interact with `aistudio.google.com`.
*   **New Permissions:** Added `tabs` and `downloads` permissions to manage the new tab and handle the image data.
*   **Keyboard Shortcut:** Introduced a `Ctrl+Shift+Q` shortcut to instantly capture the visible tab and send it to AI Studio.

#### 2. `capture.html` (The User Interface)
I added a new button to the main header, right next to the existing controls.
*   **AI Studio Button:** A new `<a>` tag with the ID `btn-aistudio` was added, featuring a "gleam" icon to represent AI.
*   **Tooltip:** Included a helpful tooltip that says "Send to AI Studio" on hover.

#### 3. `js/background/index.js` (The Background Logic)
This is where the magic happens behind the scenes.
*   **Message Listener:** The script now listens for a `sendToAIStudio` message from the capture page.
*   **Tab Management:** When a message is received, it checks if an AI Studio tab is already open.
    *   If **yes**, it focuses on that tab.
    *   If **no**, it creates a new tab and navigates to AI Studio.
*   **Script Injection:** Once the tab is ready, it injects a script (`simulateFileDrop`) that programmatically "drops" the screenshot onto the page, just as if you had dragged and dropped the file yourself!

#### 4. `capture.*.js` (The Frontend Script)
This file connects the new UI button to the background logic.
*   **Event Listener:** An `onClick` event listener was added to the new `#btn-aistudio` button.
*   **Image Processing:** When clicked, it grabs the screenshot from the page, converts it into a `dataURL` (a Base64 encoded string), and sends it to the background script for processing.

### Conclusion 🚀

This project was an amazing learning experience. It started as a simple idea to automate a course and turned into a deep dive into how Chrome extensions work. It's a great example of how, with a little curiosity, you can modify existing tools to perfectly fit your workflow.
