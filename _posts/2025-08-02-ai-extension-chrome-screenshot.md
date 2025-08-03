---
layout: post
title: One-Click Screenshot to AI- My Extension Mod 
date: 2025-08-02 00:00:00 +0300
description: A breakdown of how I modified the "GoFullPage" Chrome extension using JavaScript. This tutorial covers adding new UI elements, handling image data, and injecting scripts to automate uploading a screenshot to a third-party web application like Google AI Studio.
img: extension-mod/download.jpg # Add image post (optional)
tags: [JavaScript, ChromeExtension, GenerativeAI, Automation] # add tag
---

# My Journey: Hacking a Chrome Extension to Automate a GenAI Course 🚀

This story begins with a simple goal during my Tata micro-internship on Generative AI 🎓. I wanted to find a clever way to automate the course, by using the course material itself—specifically, the images and screenshots—as input for an AI.

### The Spark of an Idea 💡

My plan was to take full-page screenshots of the course content and feed them to a powerful AI model to summarize, analyze, or even answer questions. This felt like a practical and exciting way to apply the concepts I was learning.

### Assembling the Toolkit 🛠️

To bring this idea to life, I chose a few key tools:

*   **The AI Brain:** [**Google's AI Studio (Gemini)**](#gemini-reference-link). It's fantastic for multimodal tasks, including understanding images.
*   **The Screenshot Tool:** I needed a reliable way to capture full web pages. After a quick search, I settled on a popular Chrome extension: [**GoFullPage - Full Page Screen Capture.**](#gofullpage-reference-links)

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

### 📊 Directory Comparison Overview

<iframe src="/assets/img/extension-mod/changes.pdf" width="100%" height="600px" style="border:1px solid #ddd;">
   <p>Your browser does not support PDFs. <a href="/assets/img/extension-mod/changes.pdf">Download the PDF</a>.</p>
</iframe>

*   **📊 Directory Comparison Overview:** [Click for PDF](/assets/img/extension-mod/changes.pdf)


### 🔬 Deep Diff Analysis

For a complete line-by-line comparison, explore the interactive diff report embedded below. This shows every single code change between the original and my modified version.

<iframe src="/assets/img/extension-mod/index.html" width="100%" height="800px" style="border:1px solid #ddd; background: #fff;">
   <p>Your browser does not support iframes. <a href="/assets/img/extension-mod/index.html">View the interactive diff analysis</a>.</p>
</iframe>

*   **🔬 Deep Diff Analysis:** [View as PDF](/assets/img/extension-mod/diff.pdf)

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

---

### Bonus: My Personal Lightweight Script 🧑‍🔧

While modifying GoFullPage was a fantastic learning experience, I also developed a separate, minimalist screenshot extension from scratch. This custom script became my primary tool for the internship course because it was perfectly streamlined for one specific task: quickly capturing screenshots without any extra overhead.

It serves as a great barebones example if you're interested in building your own simple Chrome extension.

*   **Download My Custom Extension:** [**custom_extension.zip**](/assets/img/extension-mod/custom_extension.zip)

---
## References

### GoFullPage Reference Links

Here are the official links for the GoFullPage extension:

*   **Official Website:** [https://gofullpage.com/](https://gofullpage.com/)
*   **Chrome Web Store:** [https://chromewebstore.google.com/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl](https://chromewebstore.google.com/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl)

### Gemini Reference Link

* **Official Website:** [https://aistudio.google.com/prompts/new_chat](https://aistudio.google.com/prompts/new_chat)

### The Tools used for Documentation:

### - *Recursive Diff Tools:*

* **Diffoscope:** [https://try.diffoscope.org/](https://try.diffoscope.org/)

* **Diffnow:** [https://www.diffnow.com/compare-files](https://www.diffnow.com/compare-files)

### - *Document conversion Tools:*

* **Sodapdf:** [https://www.sodapdf.com/pdf-tools/html-to-pdf/](https://www.sodapdf.com/pdf-tools/html-to-pdf/)

### Extras:
### Another Great Tool Worth Mentioning: FireShot 🔥

During my research, I came across another excellent screenshot extension called **FireShot**. In some scenarios, especially on very complex or dynamic pages, I found it to be highly effective and reliable. It offers a robust set of features, making it a powerful alternative to GoFullPage.

If you're looking for another top-tier screenshot tool, I highly recommend giving it a try.

*   **Official Website:** [https://getfireshot.com/](https://getfireshot.com/)
*   **Chrome Web Store:** [https://chromewebstore.google.com/detail/take-webpage-screenshots/mcbpblocgmgfnpjjppndjkmgjaogfceg](https://chromewebstore.google.com/detail/take-webpage-screenshots/mcbpblocgmgfnpjjppndjkmgjaogfceg)
