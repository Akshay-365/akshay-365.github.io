---
layout: post
title: "URL Proxy, Blob, Local Load, Code Injection & Element Manipulation"
date: 2024-11-15 00:00:00 +0530
img: /dosbox/proxy.png # Add image post (optional)
tags: [blob,injection,proxy]
---

# 🌐 URL Proxy, Blob, Local Load, Code Injection & Element Manipulation

## ✨ A Journey Toward a Beautiful AI-Powered Presentation ✨

While working on crafting an elegant AI-generated presentation, I stumbled upon a fascinating website — [**Gamma.app**](https://gamma.app/). 🎨✨ This site offers an impressive feature:
**it allows you to transform presentations into webpages!**  🚀

---

## 🚧 The Problem Begins...

Upon using this feature, I noticed that the generated webpage included a clickable watermark (logo) acting as an advertisement. 😕 This issue is common across various free web hosting services like:
- **Vercel**
- **Netlify**
- **Ploomber.io** *etc..*

So I set off on a mission — a journey to **remove these ads via code injection**. 🕵️‍♂️💡

---

## 🧪 Experiments Conducted on Gamma.app

### 🔍 1. **Direct JS Code Injection**
Tried injecting JavaScript directly into the slide text area. Unfortunately, due to **sanitization mechanisms**, this attempt failed. ❌

### 🖼️ 2. **SVG Code Injection via Embed Option**
Gamma.app allows embedding custom files or websites using an `<iframe>`. I tried embedding an **SVG file containing malicious code** — and it worked! ✅

#### First SVG Test:
```html
<svg xmlns="http://www.w3.org/2000/svg">
  <script>alert('SVG XSS')</script>
</svg>
```

#### Another Working Payload:
```html
<img src=x onerror=alert('XSS')>
```
*But this was not enough for element alteration.*

### 💡 3. **Embedding HTML Files Directly**
*Next Approach* : I attempted embedding HTML files that included JavaScript like this:
```js
try {
    console.log(window.parent.location.href);
    console.log('✅ Can access parent document.');
} catch (e) {
    console.log('❌ Cannot access parent document:', e.message);
}
```
However, the **sandboxing of iframes** blocked access to the parent document, so I couldn't manipulate elements outside the iframe. ❌

---

## 🧭 A New Direction — Custom HTML File Approach

To overcome the limitations, I took a different route: **creating a custom HTML file** that embeds Gamma inside an iframe and then manipulates its elements directly. 🧠✨

> 🛑 Spoiler alert: **It worked!** 😉✔️

But before that... another experiment.

---

## 🧪 Offline Download & Modification

*Before finalizing the iframe approach,* I downloaded the Gamma-generated webpage to make it work offline. The page functioned offline, **but the ad button still appeared.** 🤨

To fix this, I injected a JavaScript snippet (placed inside the `<head>`) to **remove unwanted elements before they were displayed.**

### 🧼 JS Element Remover Code:
```html
<script>
<script>
(function() {
    // List of selectors to target
    const SELECTORS = [
        '.css-1c6hcbi',
        '.chakra-button__group.css-1ayoy1w'
    ];

    // Remove or hide all matching elements
    function removeTargets(root = document) {
        const els = root.querySelectorAll(SELECTORS.join(','));
        els.forEach(el => {
            el.style.display = 'none';
            el.remove();
        });
    }

    // Initial removal as soon as possible
    removeTargets();

    // Also on DOMContentLoaded and load
    document.addEventListener('DOMContentLoaded', () => removeTargets());
    window.addEventListener('load', () => removeTargets());

    // Watch for dynamically added nodes
    const observer = new MutationObserver(mutations => {
        for (const { addedNodes } of mutations) {
            addedNodes.forEach(node => {
                if (node.nodeType !== 1) return;
                // If this node itself matches
                if (node.matches && node.matches(SELECTORS.join(','))) {
                    node.style.display = 'none';
                    node.remove();
                }
                // Or any of its descendants
                removeTargets(node);
            });
        }
    });

    observer.observe(document.documentElement || document.body, {
        childList: true,
        subtree: true
    });
})();
</script>
```
✅ It worked beautifully — the ad button didn’t even flicker before being removed. A seamless experience for the user! 💨

---

## 🧩 Building the Custom Embed Page (Version 1)

Here's how I first constructed the custom HTML:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Custom Embed for Gamma Site</title>
  <style>
    html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; }
    #custom-iframe { width: 100%; height: 100%; border: none; }
  </style>
</head>
<body>
  <iframe id="custom-iframe" sandbox="allow-scripts allow-same-origin"></iframe>
  <script>
  (async function() {
    const targetUrl = 'https://meager-insect-x9oto7l.gamma.site/';
    const proxyUrl = `https://embed-proxy-prod.gamma-app.workers.dev/?alt_url=${targetUrl}`;

    try {
      console.log('Fetching proxy URL:', proxyUrl);
      const res = await fetch(proxyUrl, { mode: 'cors' });
      if (!res.ok) {
        const errorText = await res.text().catch(() => 'No response text');
        throw new Error(`Fetch failed with status ${res.status}: ${errorText}`);
      }
      let html = await res.text();
      console.log('Fetched HTML length:', html.length);

      // Injection payload: custom script to hide elements
const scriptContent = `
(function() {
  try {
    console.log('Custom embed script loaded in iframe');

    const SELECTORS = [
      '.css-1c6hcbi',
      '.chakra-button__group.css-1ayoy1w'
    ];

    function hideTargets(root = document) {
      // Make sure root is an Element or Document before calling querySelectorAll
      if (root.querySelectorAll) {
        SELECTORS.forEach(selector => {
          root.querySelectorAll(selector).forEach(el => {
            console.log('Hiding element:', el);
            el.style.display = 'none';
          });
        });
      }
    }

    function setupObserver() {
      if (!document.body) {
        console.warn('Body not ready, retrying in 100ms...');
        return setTimeout(setupObserver, 100);
      }

      hideTargets();

      const observer = new MutationObserver(mutations => {
        for (const mutation of mutations) {
          if (mutation.type === 'childList') {
            mutation.addedNodes.forEach(node => {
              if (node.nodeType === Node.ELEMENT_NODE) {
                hideTargets(node);
              }
            });
          } else if (mutation.type === 'attributes') {
            if (mutation.target.matches(SELECTORS.join(','))) {
              console.log('Hiding updated element:', mutation.target);
              mutation.target.style.display = 'none';
            }
          }
        }
      });

      observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['class']
      });

      console.log('MutationObserver set up!');
    }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
      setupObserver();
    } else {
      document.addEventListener('DOMContentLoaded', setupObserver);
    }
  } catch (err) {
    console.error('Error in injected script:', err);
  }
})();
`;

const injection = `<script>${scriptContent}<\/script>`;





      // Inject script into <head> to avoid breaking body scripts
      if (html.includes('</head>')) {
        html = html.replace(/<\/head>/i, injection + '</head>');
      } else {
        console.warn('No </head> tag found, prepending script');
        html = injection + html;
      }

      // Create Blob for same-origin iframe
      const blob = new Blob([html], { type: 'text/html' });
      const blobUrl = URL.createObjectURL(blob);

      const iframe = document.getElementById('custom-iframe');
      iframe.src = blobUrl;

      // Clean up Blob URL after load
      iframe.onload = () => {
        console.log('Iframe loaded');
        URL.revokeObjectURL(blobUrl);
      };

    } catch (err) {
      console.error('Error in fetch or injection:', err);
      document.body.innerHTML = `<p style="color:red;">Error loading content: ${err.message}</p>`;
    }
  })();
  </script>
</body>
</html>
```

### ⚠️ Problem:
- Occasionally, only the layout loaded — not the actual content. 😞 *(Don't know, this might be beacause some external error at that time.)*
- Also, **responsiveness was broken** — it didn’t adapt to screen size (stuck in desktop mode). 📱❌

---

## 🛠️ Modified Version: A Better Solution

I refined the code, resulting in the following improvements:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1"><!-- your own page remains responsive -->
  <title>Responsive Gamma Embed</title>
  <style>
    html, body { margin: 0; padding: 0; height: 100%; overflow: hidden; }
    #custom-iframe { width: 100%; height: 100%; border: none; }
  </style>
</head>
<body>
  <iframe id="custom-iframe" sandbox="allow-scripts allow-same-origin allow-top-navigation-by-user-activation allow-popups"></iframe>
  <script>
  (async function() {
    const targetUrl = 'https://scriptfunctionconst-sele-aijki1r.gamma.site/';
    const proxyUrl = `https://embed-proxy-prod.gamma-app.workers.dev/?alt_url=${targetUrl}`;

    try {
      // forward your UA so SSR can pick mobile vs desktop
      const res = await fetch(proxyUrl, {
        mode: 'cors',
        headers: {
          'Accept': 'text/html',
          'User-Agent': navigator.userAgent
        }
      });
      if (!res.ok) throw new Error(`Status ${res.status}`);
      let html = await res.text();

      // --- 1) Inject viewport meta if missing ---
      if (!/<meta\s+name=["']viewport["']/i.test(html)) {
        html = html.replace(
          /<head([^>]*)>/i,
          headTag => headTag +
            '\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        );
      }

      // --- 2) Inject your hide-elements script ---
      const scriptContent = `
      (function() {
        try {
          const SELECTORS = [
            '.css-1c6hcbi',
            '.chakra-button__group.css-1ayoy1w'
          ];
          function hideTargets(root = document) {
            if (root.querySelectorAll) {
              SELECTORS.forEach(sel => {
                root.querySelectorAll(sel).forEach(el => el.style.display = 'none');
              });
            }
          }
          function setup() {
            if (!document.body) return setTimeout(setup, 100);
            hideTargets();
            new MutationObserver(muts => {
              muts.forEach(m => {
                if (m.type === 'childList') {
                  m.addedNodes.forEach(n => {
                    if (n.nodeType === Node.ELEMENT_NODE) hideTargets(n);
                  });
                } else if (m.type === 'attributes' && m.target.matches(SELECTORS.join(','))) {
                  m.target.style.display = 'none';
                }
              });
            }).observe(document.body, {
              childList: true,
              subtree: true,
              attributes: true,
              attributeFilter: ['class']
            });
          }
          if (document.readyState !== 'loading') setup();
          else document.addEventListener('DOMContentLoaded', setup);
        } catch (e) {
          console.error('Injected script error:', e);
        }
      })();
      `;
      const injection = `<script>${scriptContent}<\/script>`;

      // add before </head> so responsive CSS & your script both load early
      if (html.match(/<\/head>/i)) {
        html = html.replace(/<\/head>/i, injection + '</head>');
      } else {
        html = injection + html;
      }

      // serve via blob so same-origin + your script can run
      const blob = new Blob([html], { type: 'text/html' });
      const url = URL.createObjectURL(blob);
      const iframe = document.getElementById('custom-iframe');
      iframe.src = url;
      iframe.onload = () => URL.revokeObjectURL(url);

    } catch (err) {
      console.error('Embed error:', err);
      document.body.innerHTML = `<p style="color:red;">Error loading embed: ${err.message}</p>`;
    }
  })();
  </script>
</body>
</html>
```

### ✅ Outcome:
- The issue of "layout only" never reoccurred *(in front of me)*.
- However, **responsiveness was still an issue.** The embedded site didn't adjust dynamically to the device screen size. 📏

*[I have included the code which is not working now]*

Despite that, the code might be beneficial in future projects where adjustments or responsive tweaks can be applied. 🌱

---

## 🔮 Future Enhancements To Be Made:

### 1. **Pre-Render Ad Removal** ✂️
The offline approach removed ad elements **before they even rendered.** 🚫
In the current final code, ads momentarily appear and then disappear — visible to the user for a split second. 😬
**Goal:** Apply the same **pre-render removal** logic to the iframe version.

### 2. **Responsive Design Inside Iframe** 📱💻
Make the embedded Gamma site **fully responsive** — adapting fluidly to various screen sizes and devices.

---

## 🏁 Conclusion

This journey was a blend of creativity, hacking, clever experimentation, and determination.
*🌈🔧 From trying SVG exploits to designing custom wrappers, each step brought valuable insights on web embedding, sandboxing, and DOM control.* ⭐

## 📚 Knowledge Application

The knowledge from this experiment can be useful in other cases such as:

**🔧 Embedding third-party websites or apps hosted elsewhere into local wrappers, with control over visual layout and ad suppression, for a custom user experience, control and element manipulation, etc.**
