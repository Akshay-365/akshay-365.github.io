---
layout: post
title: Chrome Dino.
date: 2025-01-05 00:00:00 +0300
img: chrome-dino.jpg # Add image post (optional)
tags: [Programming, Learn] # add tag
---

<iframe src="https://astraos-chromedino.static.hf.space/index.html"
        width="100%" 
        height="600px" 
        frameborder="0"
        allow="autoplay; picture-in-picture; fullscreen"
        allowfullscreen
        sandbox="allow-scripts allow-same-origin allow-popups"
        loading="lazy"
        style="border: none; margin: 0; padding: 0;">
</iframe>

<!-- Include the CSS for styling -->
<link rel="stylesheet" href="{{ '/assets/chromeDino/style.css' | relative_url }}">

<!-- Create a container where the HTML content will go -->
<div id="game-container"></div>

<script>
// Fetch the HTML content and insert it into the container
fetch('{{ '/assets/chromeDino/index.html' | relative_url }}')
  .then(response => response.text())
  .then(html => {
    document.getElementById('game-container').innerHTML = html;
  })
  .catch(error => console.error('Error loading HTML:', error));
</script>
