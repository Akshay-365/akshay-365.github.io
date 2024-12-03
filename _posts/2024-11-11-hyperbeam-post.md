---
layout: post
title: "My Hyperbeam Post"
date: 2024-12-03
---

<div id="container"></div>

<style>
    html, body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        overflow: hidden; /* Hide scrollbars */
    }

    ::-webkit-scrollbar {
        width: 0; /* Hide scrollbar */
    }

    #container {
        width: 100vw; /* Set width to match viewport width */
        height: calc(56.25vw); /* Set height to maintain aspect ratio (16:9) */
        position: relative;
    }
</style>

<script type="module">
    import Hyperbeam from 'https://unpkg.com/@hyperbeam/web@latest/dist/index.js';

    const container = document.getElementById('container');

    async function initHyperbeam() {
        const embedURL = "https://8k5w12dgn9f4hsi5uiprvoyqg.hyperbeam.com/HBqAFBwARAat8agg7qL6Nw?token=SUK9LpbAw7XXxOSVUK1tEVbnQ4flXo3bi8SXP6bQZoQ";
        const hb = await Hyperbeam(container, embedURL);
        hb.onLoad(adjustDimensions);
        window.addEventListener('resize', adjustDimensions);
    }

    function adjustDimensions() {
        container.style.width = `${window.innerWidth}px`;
        container.style.height = `calc(${window.innerWidth * 0.5625}px)`;
    }

    initHyperbeam();
</script>
