


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
