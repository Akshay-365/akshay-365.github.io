---
layout: post
title: "Online Video Player"
date: 2024-11-21 14:00:00
description: Online video player platform. # Add post description (optional)
img: /video_player.jpg # Add image post (optional)
categories: video streaming
tags: [video, stream , favourite, pin]
---

<link rel="stylesheet" href="/assets/css/DPlayer.min.css">
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

<script src="/assets/js/DPlayer.min.js"></script>

<script>
  // Initialize DPlayer with the default MP4 video URL
  const player = new DPlayer({
      element: document.getElementById('dplayer-container'),
       screenshot: true,
    //    autoplay: true,
       preload: 'auto',
       logo: '/assets/img/profile-pic.png',
       subtitle: {
         url: 'dplayer.vtt',
         type: 'webvtt',
         fontSize: '25px',
         bottom: '10%',
         color: '#b7daff',
        },

       video: {
          url: 'https://live-par-2-abr.livepush.io/vod/bigbuckbunnyclip.mp4',
          pic: '/assets/img/default_img.png',
          type: 'auto',
       }
  });

  // Update video source when the "Play" button is clicked
  document.getElementById('player-play-btn').addEventListener('click', function () {
      const videoUrl = document.getElementById('player-url').value; // Get URL from input
      player.switchVideo({ url: videoUrl, type: 'mp4' }); // Switch to new video URL
  });
</script>

<link rel="stylesheet" href="/assets/css/dplayer_styles.css">

[Github](https://github.com/DIYgod/DPlayer)
