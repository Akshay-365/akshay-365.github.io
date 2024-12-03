---
layout: post
title: vbrowser World!
date: 2024-11-24 00:00:00 +0300
description: # Add post description (optional)
img: hello-world.jpg # Add image post (optional)
tags: [Programming, Learn] # add tag
---

# Here we go!

            <div>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Hyperbeam Example</title>
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
            </head>
            <body>
                <div id="container"></div>

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
            </body>
            </div>
        
