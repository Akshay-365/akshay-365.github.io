---
layout: post
title: "Noise"
date: 2024-11-15 00:00:00 +0530
img: noise.jpg # Add figcaption (optional)
tags: [noise,gaussian,wave,fluid]
---


noise:

```
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Noise Effect</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      min-height: 100vh;
      background: white;
      position: relative;
      overflow: hidden;
    }

    .noise-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      filter: url(#noise);
      pointer-events: none;
      background: rgba(0, 0, 0, 0.1);
    }

    .noise-svg {
      position: fixed;
      width: 0;
      height: 0;
    }
  </style>
</head>
<body>
  <div class="noise-container"></div>
  
  <svg class="noise-svg">
    <defs>
      <filter id='noise'>
        <feTurbulence 
          type='fractalNoise' 
          baseFrequency='0.85' 
          numOctaves='4' 
          stitchTiles='stitch'/>
        <feColorMatrix
          type="saturate"
          values="0.15"/>
        <feComponentTransfer>
          <feFuncR type="discrete" tableValues="0 0.5 1"/>
          <feFuncG type="discrete" tableValues="0 0.5 1"/>
          <feFuncB type="discrete" tableValues="0 0.5 1"/>
        </feComponentTransfer>
        <feGaussianBlur stdDeviation="0.5"/>
        <feBlend
          mode="overlay"
          in="SourceGraphic"
          result="blend"/>
      </filter>
    </defs>
  </svg>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const noiseFilter = document.querySelector('#noise feTurbulence');
      let seed = Math.random() * 100;
      
      function updateNoise() {
        if (!noiseFilter) return;
        
        seed += 0.002;
        const baseFreq = 0.85 + Math.sin(seed) * 0.02;
        const numOctaves = 4 + Math.sin(seed * 0.7) * 0.5;
        
        noiseFilter.setAttribute('baseFrequency', `${baseFreq} ${baseFreq}`);
        noiseFilter.setAttribute('numOctaves', numOctaves);
        
        if (Math.random() < 0.1) {
          noiseFilter.setAttribute('seed', Math.floor(Math.random() * 100));
        }
        
        requestAnimationFrame(updateNoise);
      }

      updateNoise();
    });
  </script>
</body>
</html>

```

All started with `https://deta.surf/`

inspiration there is `https://upload.wikimedia.org/wikipedia/commons/5/5c/Image_gaussian_noise_example.png`

and i like it's footer `https://deta.surf/footer-32-yesdither-nomatte.gif`

# wavy effect:
```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wavy Noise Exploration</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: flex-start;
            background-color: #f0f0f0;
            padding: 20px;
            gap: 20px;
        }

        .noise-container {
            width: calc(100% - 20px);
            height: 500px;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .noise-container:hover {
            transform: scale(1.05);
        }

        .noise-title {
            position: absolute;
            top: 10px;
            left: 10px;
            font-family: Arial, sans-serif;
            font-size: 1rem;
            color: #333;
            z-index: 10;
        }

        .noise-svg {
            position: fixed;
            width: 0;
            height: 0;
        }

        .text-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 5em;
            font-weight: bold;
            color: #222;
            filter: url(#water-effect);
        }
    </style>
</head>
<body>
    <svg class="noise-svg">
        <defs>
            <filter id='noise-wavy'>
                <feTurbulence type='fractalNoise' baseFrequency='0.025' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="4.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.04"/>
            </filter>
            <filter id="water-effect">
                <feTurbulence type="fractalNoise" baseFrequency="0.008" numOctaves="1" stitchTiles="stitch"/>
                <feDisplacementMap in="SourceGraphic" scale="6.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
        </defs>
    </svg>
    <div class="noise-container" style="filter: url(#noise-wavy);">
        <span class="noise-title">Wavy Noise</span>
        <div class="text-container">
            Hello World
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const noiseFilter = document.querySelector('#noise-wavy > feTurbulence');
            const waterFilter = document.querySelector('#water-effect > feTurbulence');

            function createWavyAnimation(filter) {
                if (!filter) return;

                let time = 0;
                function animate() {
                    time += 0.01;
                    
                    // Subtle density variation with smooth oscillation
                    const baseFrequency = parseFloat(filter.getAttribute('baseFrequency'));
                    const densityVariation = Math.sin(time) * 0.0008;
                    
                    // Limit the density variation to a very small range
                    const dynamicFrequency = Math.max(0.005, Math.min(baseFrequency + densityVariation, baseFrequency * 1.2));
                    
                    filter.setAttribute('baseFrequency', `${dynamicFrequency} ${dynamicFrequency}`);
                    
                    requestAnimationFrame(animate);
                }
                animate();
            }

            createWavyAnimation(noiseFilter);
            createWavyAnimation(waterFilter);
        });
    </script>
</body>
</html>
```
## Wavy effect comparison:
```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wavy Noise Water Effect Comparison</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: flex-start;
            background-color: #f0f0f0;
            padding: 20px;
            gap: 20px;
        }

        .noise-container {
            width: calc(33.33% - 20px);
            height: 300px;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .noise-container:hover {
            transform: scale(1.05);
        }

        .noise-title {
            position: absolute;
            top: 10px;
            left: 10px;
            font-family: Arial, sans-serif;
            font-size: 1rem;
            color: #333;
            z-index: 10;
        }

        .text-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 2em;
            font-weight: bold;
            color: #222;
        }

        .noise-svg {
            position: fixed;
            width: 0;
            height: 0;
        }
    </style>
</head>
<body>
    <svg class="noise-svg">
        <defs>
            <!-- Noise Wavy Filters -->
            <filter id='noise-wavy-1'>
                <feTurbulence type='fractalNoise' baseFrequency='0.015' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.04"/>
            </filter>

            <!-- Water Effect Filters -->
            <filter id='water-effect-1'>
                <feTurbulence type='fractalNoise' baseFrequency='0.008' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="4.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
            <filter id='water-effect-2'>
                <feTurbulence type='fractalNoise' baseFrequency='0.009' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
            <filter id='water-effect-3'>
                <feTurbulence type='fractalNoise' baseFrequency='0.01' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
            <filter id='water-effect-4'>
                <feTurbulence type='fractalNoise' baseFrequency='0.011' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="4.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
            <filter id='water-effect-5'>
                <feTurbulence type='fractalNoise' baseFrequency='0.012' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
            <filter id='water-effect-6'>
                <feTurbulence type='fractalNoise' baseFrequency='0.007' numOctaves='1' stitchTiles='stitch'/>
                <feDisplacementMap in="SourceGraphic" scale="3.5" xChannelSelector="R" yChannelSelector="G"/>
                <feColorMatrix type="saturate" values="0.03"/>
            </filter>
        </defs>
    </svg>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 1</span>
        <div class="text-container" style="filter: url(#water-effect-1)">
            Hello World
        </div>
    </div>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 2</span>
        <div class="text-container" style="filter: url(#water-effect-2)">
            Hello World
        </div>
    </div>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 3</span>
        <div class="text-container" style="filter: url(#water-effect-3)">
            Hello World
        </div>
    </div>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 4</span>
        <div class="text-container" style="filter: url(#water-effect-4)">
            Hello World
        </div>
    </div>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 5</span>
        <div class="text-container" style="filter: url(#water-effect-5)">
            Hello World
        </div>
    </div>

    <div class="noise-container" style="filter: url(#noise-wavy-1);">
        <span class="noise-title">Wavy Noise 6</span>
        <div class="text-container" style="filter: url(#water-effect-6)">
            Hello World
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const noiseFilters = document.querySelectorAll('svg > defs > filter[id^="noise-wavy-"] > feTurbulence');
            const waterFilters = document.querySelectorAll('svg > defs > filter[id^="water-effect-"] > feTurbulence');

            function createWavyAnimation(filter, isWater = false) {
                if (!filter) return;

                let time = 0;
                let amplitudeDirection = 1;
                function animate() {
                    time += 0.01;
                    
                    // Subtle density variation with smooth oscillation
                    const baseFrequency = parseFloat(filter.getAttribute('baseFrequency'));
                    const densityVariation = Math.sin(time) * 0.0007;
                    
                    // Limit the density variation to a very small range
                    const dynamicFrequency = Math.max(0.005, Math.min(baseFrequency + densityVariation, baseFrequency * 1.2));
                    
                    filter.setAttribute('baseFrequency', `${dynamicFrequency} ${dynamicFrequency}`);
                    
                    requestAnimationFrame(animate);
                }
                animate();
            }

            // Animate noise and water filters with continuous, subtle movement
            noiseFilters.forEach(filter => createWavyAnimation(filter, false));
            waterFilters.forEach(filter => createWavyAnimation(filter, true));
        });
    </script>
</body>
</html>
```
