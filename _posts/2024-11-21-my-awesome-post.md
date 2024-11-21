---
layout: post
title: "Test MP4 URLs with DPlayer"
date: 2024-11-21 14:00:00
categories: video streaming
---

<div class="header section_wrap" style="height:auto; justify-content:flex-start;">
    <div class="container section_layout section_layout_feature section_layout_vertical">
        <div class="header-title-section">
            <h1 class="header-title">Dplayer Stream</h1>
            <h3 class="header-title-text">MP4, HLS stream URLs with our faster HTML5 player</h3>
        </div>
        <div class="content_wrap content_wrap_player_wrap">
            <button class="btn-type btn-type-tab form-btn active" data-playback-type="mp4" type="button">MP4 Player</button>

            <div class="form-grp">
                <input id="player-url" class="form-input" value="https://live-par-2-abr.livepush.io/vod/bigbuckbunnyclip.mp4" placeholder="Enter your MP4 / HLS / DASH URL to test">
                <button id="player-play-btn" class="form-btn" type="button">Play <span id="extname">MP4</span></button>
            </div>

            <!-- DPlayer container -->
            <div id="dplayer-container" style="width: 100%; max-width: 720px; height: 405px; margin-top: 20px;"></div>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/dplayer/dist/DPlayer.min.js"></script>

<script>
  // Initialize DPlayer with the default MP4 video URL
  const player = new DPlayer({
      element: document.getElementById('dplayer-container'),
      video: {
          url: 'https://live-par-2-abr.livepush.io/vod/bigbuckbunnyclip.mp4',
      }
  });

  // Update video source when the "Play" button is clicked
  document.getElementById('player-play-btn').addEventListener('click', function () {
      const videoUrl = document.getElementById('player-url').value; // Get URL from input
      player.switchVideo({ url: videoUrl, type: 'mp4' }); // Switch to new video URL
  });
</script>

