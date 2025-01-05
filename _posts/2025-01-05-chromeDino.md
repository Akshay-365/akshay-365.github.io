---
layout: post
title: Chrome Dino.
date: 2025-01-05 00:00:00 +0300
img: chrome-dino.jpg # Add image post (optional)
tags: [Programming, Learn] # add tag
---

<!-- <iframe src="https://astraos-chromedino.static.hf.space/index.html"
        width="100%" 
        height="600px" 
        frameborder="0"
        allow="autoplay; picture-in-picture; fullscreen"
        allowfullscreen
        sandbox="allow-scripts allow-same-origin allow-popups"
        loading="lazy"
        style="border: none; margin: 0; padding: 0;">
</iframe> -->

<!-- Include the CSS for styling -->
<link rel="stylesheet" href="{{ '/assets/chromeDino/style.css' | relative_url }}">

<!-- Create a container where the HTML content will go -->
<div id="game-container" class="game-container">
  <!-- Loading spinner while content is being fetched -->
  <div id="loading-spinner" class="loading-spinner">
    <div class="spinner"></div>
    <p>Loading game, please wait...</p>
  </div>
  
  <!-- Fallback message if HTML content cannot be loaded -->
  <div id="error-message" class="error-message" style="display: none;">
    <p>Sorry, the game could not be loaded. Please try again later.</p>
  </div>
</div>

<script>
// Function to load the HTML content dynamically
function loadGameContent() {
  // Show the loading spinner initially
  document.getElementById('loading-spinner').style.display = 'block';
  document.getElementById('game-container').style.display = 'none'; // Hide game container initially
  
  // Fetch the HTML content
  fetch('{{ '/assets/chromeDino/index.html' | relative_url }}')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to load HTML');
      }
      return response.text();
    })
    .then(html => {
      // Hide the loading spinner and show the game container
      document.getElementById('loading-spinner').style.display = 'none';
      document.getElementById('game-container').style.display = 'block';
      
      // Insert the fetched HTML content into the container
      document.getElementById('game-container').innerHTML = html;
      
      // Initialize any necessary JavaScript for the game
      initializeGame();
    })
    .catch(error => {
      // Hide the loading spinner and show the error message
      document.getElementById('loading-spinner').style.display = 'none';
      document.getElementById('error-message').style.display = 'block';
      
      // Log the error for debugging
      console.error('Error loading HTML:', error);
    });
}

// Initialize the game (this could be a function within the embedded HTML)
function initializeGame() {
  // Example: Adding event listeners or other interactive features
  const canvas = document.getElementById('gameCanvas');
  const ctx = canvas.getContext('2d');
  // Your game logic here (e.g., start game loop)
  console.log('Game initialized!');
}

// Call the function to load the game content
loadGameContent();
</script>

<!-- Add your custom styles for the game container and loading spinner -->
<style>
/* Style for the game container */
.game-container {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  display: none; /* Initially hidden until content is loaded */
}

/* Loading spinner styling */
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 50px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-spinner p {
  margin-top: 10px;
  font-size: 16px;
}

/* Error message styling */
.error-message {
  color: red;
  font-size: 18px;
  font-weight: bold;
}
</style>

