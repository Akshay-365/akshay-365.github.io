<main class="relative flex min-h-0 flex-auto flex-grow flex-col">
	<div class="react-scroll-to-bottom--css-ciikt-79elbk h-full">
		<div class="react-scroll-to-bottom--css-ciikt-1n7m0yu flex flex-col">
			<div class="block">
				<div class="h-full w-full">
					<div class="flex h-full justify-center" style="margin: 0px 36px; padding-top: 66.08px; will-change: auto;">
						<div class="z-0 flex w-full flex-col items-center">
							<div id="prosemirror-context-children"></div>
							<div class="relative z-10 flex max-w-full h-fit" id="prosemirror-editor-container" style="padding-bottom: max(3rem, 24vh);">
								<div class="_main_5jn6z_1 z-10 markdown prose contain-inline-size dark:prose-invert focus:outline-none bg-transparent ProseMirror" contenteditable="true" style="width: 580px;" translate="no">
									<div contenteditable="false">
										<hr>
										</div>
										<h2>
											<span>layout: post title: GUI remote desktop date: 2025-01-23 00:00:00 +0300 img: hello-world.jpg # Add image post (optional) tags: [GUI, ssh, remote, xfce] # add tag</span>
										</h2>
										<h1>
											<span>🖥️ HOW CAN YOU HAVE A DESKTOP REMOTE ENVIRONMENT</span>
										</h1>
										<p>
											<span>
												<em>(Focuses on XFCE4 / XFCE4-session for some xstartup commands.)</em>
											</span>
										</p>
										<h2>
											<span>🔧 Step 1: Update and Install Required Packages</span>
										</h2>
										<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ61" data-is-code-block-view="true" contenteditable="false">
											<div class="cm-announced" aria-live="polite"></div>
											<div tabindex="-1" class="cm-scroller">
												<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
													<div class="cm-line">apt update &amp;&amp; apt upgrade 
														<span class="ͼ2u">-y</span>
													</div>
													<div class="cm-line">apt install 
														<span class="ͼ2u">-y</span> xfce4 xfce4-goodies tigervnc-standalone-server 
														<span class="ͼ2u">wget</span>
														<span class="ͼ2u">curl</span>
														<span class="ͼ2u">git</span> dbus-x11
													</div>
												</div>
												<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms; transform: scale(1, 1);">
													<div class="cm-cursor cm-cursor-primary" style="left: 6px; top: 5.59998px; height: 18.4px;"></div>
												</div>
												<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2; transform: scale(1, 1);"></div>
											</div>
										</div>
										<h2>
											<span>🔑 Step 2: Create a VNC Password for the Server</span>
										</h2>
										<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ62" data-is-code-block-view="true" contenteditable="false">
											<div class="cm-announced" aria-live="polite"></div>
											<div tabindex="-1" class="cm-scroller">
												<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
													<div class="cm-line">vncpasswd</div>
												</div>
												<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms; transform: scale(1, 1);">
													<div class="cm-cursor cm-cursor-primary" style="left: 6px; top: 5.60004px; height: 18.4px;"></div>
												</div>
												<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2; transform: scale(1, 1);"></div>
											</div>
										</div>
										<h2>
											<span>📥 Step 3: Clone the noVNC Repository</span>
										</h2>
										<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ63" data-is-code-block-view="true" contenteditable="false">
											<div class="cm-announced" aria-live="polite"></div>
											<div tabindex="-1" class="cm-scroller">
												<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
													<div class="cm-line">
														<span class="ͼ2u">git</span> clone https://github.com/novnc/noVNC.git /opt/novnc
													</div>
												</div>
												<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
													<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
												</div>
												<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
											</div>
										</div>
										<h2>
											<span>📂 Step 4: Navigate to the noVNC Directory</span>
										</h2>
										<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ64" data-is-code-block-view="true" contenteditable="false">
											<div class="cm-announced" aria-live="polite"></div>
											<div tabindex="-1" class="cm-scroller">
												<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
													<div class="cm-line">
														<span class="ͼ2u">cd</span> /opt/novnc/utils
													</div>
													<div class="cm-line">
														<span class="ͼ2u">ln</span>
														<span class="ͼ2u">-s</span> ../novnc_proxy .
													</div>
												</div>
												<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
													<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48798px; height: 18.032px;"></div>
												</div>
												<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
											</div>
										</div>
										<h2>
											<span>🚀 Step 5: Run noVNC</span>
										</h2>
										<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ65" data-is-code-block-view="true" contenteditable="false">
											<div class="cm-announced" aria-live="polite"></div>
											<div tabindex="-1" class="cm-scroller">
												<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
													<div class="cm-line">/opt/novnc/utils/novnc_proxy 
														<span class="ͼ2u">--vnc</span> localhost:5901
													</div>
												</div>
												<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
													<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
												</div>
												<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
											</div>
										</div>
										<div contenteditable="false">
											<hr>
											</div>
											<h2>
												<span>🏆 Preferred Way (xstartup)</span>
											</h2>
											<h3>
												<span>✅ Confirm Desktop is Enabled</span>
											</h3>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ66" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ2s ͼb">export</span>
															<span class="ͼ2u ͼg">DISPLAY</span>
															<span class="ͼ2z">=</span>:1
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<p>
												<span>Check with:</span>
											</p>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ67" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ2u">echo</span>
															<span class="ͼ2u ͼg">$DISPLAY</span>
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48792px; height: 18.0321px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<h3>
												<span>📂 Navigate to </span>
												<code>
													<span>.vnc</span>
												</code>
												<span> Folder</span>
											</h3>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ68" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ2u">ls</span>
															<span class="ͼ2u">-la</span>
														</div>
														<div class="cm-line">
															<span class="ͼ2u">cd</span> .vnc
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<h3>
												<span>📝 Create xstartup File</span>
											</h3>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ69" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">nano xstartup</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<p>
												<span>📜 </span>
												<span>
													<strong>Content of </strong>
												</span>
												<span>
													<strong>
														<strong>
															<strong>``</strong>
														</strong>
													</strong>
												</span>
												<span>
													<strong> for a VNCServer with XFCE Desktop:</strong>
												</span>
											</p>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6a" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ36 ͼ5">#!/bin/sh</span>
														</div>
														<div class="cm-line">
															<span class="ͼ2s ͼb">unset</span> SESSION_MANAGER
														</div>
														<div class="cm-line">
															<span class="ͼ2s ͼb">unset</span> DBUS_SESSION_BUS_ADDRESS
														</div>
														<div class="cm-line">/usr/bin/startxfce4</div>
														<div class="cm-line">[ 
															<span class="ͼ2u">-x</span> /etc/vnc/xstartup ] &amp;&amp; exec /etc/vnc/xstartup
														</div>
														<div class="cm-line">x-window-manager &amp;</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<h3>
												<span>🔧 Set Executable Permissions</span>
											</h3>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6b" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ2u">chmod</span>
															<span class="ͼ2z">+</span>x /root/.vnc/xstartup
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0319px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<p>
												<span>(Optional):</span>
											</p>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6c" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">
															<span class="ͼ2u">chown</span> root:root /root/.vnc/xstartup
														</div>
														<div class="cm-line">
															<span class="ͼ2u">chmod</span>
															<span class="ͼ2y ͼd">755</span> /root/.vnc/xstartup
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<h3>
												<span>🚀 Start VNC Server</span>
											</h3>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6d" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">vncserver :1</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0317px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<p>
												<span>To kill VNC Server:</span>
											</p>
											<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6e" data-is-code-block-view="true" contenteditable="false">
												<div class="cm-announced" aria-live="polite"></div>
												<div tabindex="-1" class="cm-scroller">
													<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
														<div class="cm-line">vncserver 
															<span class="ͼ2u">-kill</span> :1
														</div>
													</div>
													<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
														<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.0317px;"></div>
													</div>
													<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
												</div>
											</div>
											<p>
												<span>🔗 </span>
												<span>
													<strong>Open port </strong>
												</span>
												<span>
													<strong>
														<strong>
															<strong>``</strong>
														</strong>
													</strong>
												</span>
												<span>
													<strong> (or the assigned one) in your browser and enjoy!</strong>
												</span>
											</p>
											<div contenteditable="false">
												<hr>
												</div>
												<h2>
													<span>🔄 Alternative Ways</span>
												</h2>
												<h3>
													<span>⚡ If </span>
													<code>
														<span>vncserver :1</span>
													</code>
													<span> Gives Errors:</span>
												</h3>
												<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6f" data-is-code-block-view="true" contenteditable="false">
													<div class="cm-announced" aria-live="polite"></div>
													<div tabindex="-1" class="cm-scroller">
														<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
															<div class="cm-line">tigervncserver 
																<span class="ͼ2u">-xstartup</span> /usr/bin/xterm
															</div>
														</div>
														<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
															<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
														</div>
														<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
													</div>
												</div>
												<p>
													<span>Then in the noVNC virtual terminal:</span>
												</p>
												<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6g" data-is-code-block-view="true" contenteditable="false">
													<div class="cm-announced" aria-live="polite"></div>
													<div tabindex="-1" class="cm-scroller">
														<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
															<div class="cm-line">xfce4-session 
																<span class="ͼ2u">--display</span>
																<span class="ͼ2z">=</span>:1
															</div>
														</div>
														<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
															<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.032px;"></div>
														</div>
														<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
													</div>
												</div>
												<h3>
													<span>🖥️ Running Apps Without Full Desktop</span>
												</h3>
												<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6h" data-is-code-block-view="true" contenteditable="false">
													<div class="cm-announced" aria-live="polite"></div>
													<div tabindex="-1" class="cm-scroller">
														<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
															<div class="cm-line">apt install 
																<span class="ͼ2u">-y</span> x11-apps
															</div>
															<div class="cm-line">xclock</div>
														</div>
														<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
															<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.0317px;"></div>
														</div>
														<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
													</div>
												</div>
												<h3>
													<span>❌ Without Using </span>
													<code>
														<span>xstartup</span>
													</code>
												</h3>
												<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6i" data-is-code-block-view="true" contenteditable="false">
													<div class="cm-announced" aria-live="polite"></div>
													<div tabindex="-1" class="cm-scroller">
														<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
															<div class="cm-line">vncserver :1</div>
															<div class="cm-line">xfce4-session 
																<span class="ͼ2u">--display</span>
																<span class="ͼ2z">=</span>:1
															</div>
														</div>
														<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
															<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.0322px;"></div>
														</div>
														<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
													</div>
												</div>
												<p>
													<span>To stop XFCE4:</span>
												</p>
												<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6j" data-is-code-block-view="true" contenteditable="false">
													<div class="cm-announced" aria-live="polite"></div>
													<div tabindex="-1" class="cm-scroller">
														<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
															<div class="cm-line">xfce4-session-logout 
																<span class="ͼ2u">--logout</span>
															</div>
														</div>
														<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
															<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
														</div>
														<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
													</div>
												</div>
												<div contenteditable="false">
													<hr>
													</div>
													<h2>
														<span>🔥 HOT: Use SSH with X11 Forwarding (For GUI Apps)</span>
													</h2>
													<p>
														<span>Run GUI Apps from the Container:</span>
													</p>
													<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6k" data-is-code-block-view="true" contenteditable="false">
														<div class="cm-announced" aria-live="polite"></div>
														<div tabindex="-1" class="cm-scroller">
															<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																<div class="cm-line">apt install 
																	<span class="ͼ2u">-y</span> openssh-server
																</div>
																<div class="cm-line">
																	<span class="ͼ2u">ssh</span>
																	<span class="ͼ2u">-X</span> user@localhost 
																	<span class="ͼ2u">-p</span>
																	<span class="ͼ2y ͼd">2222</span>
																</div>
															</div>
															<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
															</div>
															<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
														</div>
													</div>
													<p>
														<span>
															<em>(Modify accordingly 😎.)</em>
														</span>
													</p>
													<div contenteditable="false">
														<hr>
														</div>
														<h2>
															<span>🛠️ TIPS: Use </span>
															<code>
																<span>-geometry</span>
															</code>
															<span> for Resolution Adjustment</span>
														</h2>
														<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6l" data-is-code-block-view="true" contenteditable="false">
															<div class="cm-announced" aria-live="polite"></div>
															<div tabindex="-1" class="cm-scroller">
																<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																	<div class="cm-line">vncserver :1 
																		<span class="ͼ2u">-geometry</span> 1535x824
																	</div>
																</div>
																<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																	<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.0322px;"></div>
																</div>
																<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
															</div>
														</div>
														<p>
															<span>
																<em>(For my laptop.)</em>
															</span>
														</p>
														<div contenteditable="false">
															<hr>
															</div>
															<h2>
																<span>🌐 Inside GUI Desktop: Installing a Browser</span>
															</h2>
															<p>
																<span>To install </span>
																<span>
																	<strong>Falkon</strong>
																</span>
																<span>:</span>
															</p>
															<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6m" data-is-code-block-view="true" contenteditable="false">
																<div class="cm-announced" aria-live="polite"></div>
																<div tabindex="-1" class="cm-scroller">
																	<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																		<div class="cm-line">apt install falkon</div>
																	</div>
																	<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																		<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48779px; height: 18.032px;"></div>
																	</div>
																	<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
																</div>
															</div>
															<p>
																<span>🔹 </span>
																<span>
																	<strong>Fixing Browser Launch Issues:</strong>
																</span>
															</p>
															<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6n" data-is-code-block-view="true" contenteditable="false">
																<div class="cm-announced" aria-live="polite"></div>
																<div tabindex="-1" class="cm-scroller">
																	<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																		<div class="cm-line">
																			<span class="ͼ2u">cd</span> /usr/bin/
																		</div>
																		<div class="cm-line">
																			<span class="ͼ2u">sudo</span> env 
																			<span class="ͼ2u ͼg">QTWEBENGINE_DISABLE_SANDBOX</span>
																			<span class="ͼ2z">=</span>
																			<span class="ͼ2y ͼd">1</span> ./MyApp
																		</div>
																	</div>
																	<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																		<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.0315px;"></div>
																	</div>
																	<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
																</div>
															</div>
															<p>
																<span>
																	<em>(Replace </em>
																</span>
																<code>
																	<span>
																		<strong>
																			<em>** with **</em>
																		</strong>
																	</span>
																</code>
																<span>
																	<em> or any other browser.)</em>
																</span>
															</p>
															<h3>
																<span>🆕 Alternative: Creating a Sub-User</span>
															</h3>
															<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6o" data-is-code-block-view="true" contenteditable="false">
																<div class="cm-announced" aria-live="polite"></div>
																<div tabindex="-1" class="cm-scroller">
																	<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																		<div class="cm-line">
																			<span class="ͼ2u">sudo</span> adduser newuser_name
																		</div>
																	</div>
																	<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																		<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48828px; height: 18.032px;"></div>
																	</div>
																	<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
																</div>
															</div>
															<p>
																<span>Then test with:</span>
															</p>
															<div class="cm-editor ͼ1 ͼ3 ͼ4 ͼ2r ͼ6p" data-is-code-block-view="true" contenteditable="false">
																<div class="cm-announced" aria-live="polite"></div>
																<div tabindex="-1" class="cm-scroller">
																	<div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" role="textbox" aria-multiline="true" data-language="shell" style="tab-size: 4;">
																		<div class="cm-line">./MyApp 
																			<span class="ͼ2u">--no</span>
																			<span class="ͼ2u">-sandbox</span>
																		</div>
																	</div>
																	<div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;">
																		<div class="cm-cursor cm-cursor-primary" style="left: 5.88004px; top: 5.48804px; height: 18.032px;"></div>
																	</div>
																	<div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div>
																</div>
															</div>
															<p>
																<span>🚀 </span>
																<span>
																	<strong>Enjoy Your Remote GUI Desktop!</strong>
																</span>
															</p>
															<p>
																<br class="ProseMirror-trailingBreak">
																</p>
															</div>
															<div aria-hidden="true" class="pointer-events-none invisible fixed left-0 top-0 h-0 overflow-clip">
																<div>
																	<div role="toolbar" aria-orientation="horizontal" dir="ltr" class="m-0 flex h-10 w-fit min-w-0 flex-shrink items-center overflow-hidden rounded-xl border border-token-border-light bg-token-main-surface-primary shadow-xl p-1" tabindex="0" data-orientation="horizontal" style="outline: none;">
																		<button type="button" disabled="" class="flex h-full items-center gap-1 rounded-lg px-2.5 hover:bg-[#f5f5f5] disabled:opacity-50 disabled:cursor-not-allowed dark:hover:bg-token-main-surface-secondary disabled:hover:bg-transparent" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">
																			<svg width="24" height="24" viewBox="0 0 24 24" fill="none"
																				xmlns="http://www.w3.org/2000/svg" class="icon-sm mr-0.5 text-token-text-tertiary">
																				<path fill-rule="evenodd" clip-rule="evenodd" d="M12 4.5C7.5271 4.5 4 7.91095 4 12C4 13.6958 4.5996 15.263 5.62036 16.5254C5.80473 16.7534 5.87973 17.0509 5.82551 17.339C5.72928 17.8505 5.60336 18.3503 5.45668 18.8401C6.08722 18.743 6.69878 18.6098 7.2983 18.4395C7.54758 18.3687 7.81461 18.3975 8.04312 18.5197C9.20727 19.1423 10.5566 19.5 12 19.5C16.4729 19.5 20 16.0891 20 12C20 7.91095 16.4729 4.5 12 4.5ZM2 12C2 6.70021 6.53177 2.5 12 2.5C17.4682 2.5 22 6.70021 22 12C22 17.2998 17.4682 21.5 12 21.5C10.3694 21.5 8.82593 21.1286 7.46141 20.4675C6.36717 20.7507 5.2423 20.9253 4.06155 20.9981C3.72191 21.019 3.39493 20.8658 3.19366 20.5915C2.9924 20.3171 2.94448 19.9592 3.06647 19.6415C3.35663 18.8859 3.6004 18.1448 3.77047 17.399C2.65693 15.8695 2 14.0088 2 12ZM12 8C12.5523 8 13 8.44772 13 9V11H15C15.5523 11 16 11.4477 16 12C16 12.5523 15.5523 13 15 13H13V15C13 15.5523 12.5523 16 12 16C11.4477 16 11 15.5523 11 15V13H9C8.44772 13 8 12.5523 8 12C8 11.4477 8.44772 11 9 11H11V9C11 8.44772 11.4477 8 12 8Z" fill="currentColor"></path>
																			</svg>
																			<span class="truncate text-sm text-token-text-primary">Ask ChatGPT</span>
																		</button>
																		<div data-orientation="vertical" aria-orientation="vertical" role="separator" class="mx-1 p-0 list-none h-full w-[1px] bg-token-border-light"></div>
																		<button type="button" aria-label="Bold" class="flex h-full items-center gap-1 rounded-lg px-2.5 hover:bg-[#f5f5f5] disabled:opacity-50 disabled:cursor-not-allowed dark:hover:bg-token-main-surface-secondary disabled:hover:bg-transparent" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">
																			<svg width="16" height="17" viewBox="0 0 16 17" fill="none"
																				xmlns="http://www.w3.org/2000/svg" class="icon-sm text-token-text-primary">
																				<path d="M5.11619 13.8334C4.41395 13.8334 4 13.4047 4 12.6655V4.32729C4 3.59548 4.41395 3.16675 5.11619 3.16675H8.64218C10.6454 3.16675 11.9021 4.19424 11.9021 5.82787C11.9021 6.99581 11.0298 7.97155 9.89882 8.14157V8.20071C11.3477 8.31158 12.4121 9.36864 12.4121 10.7805C12.4121 12.6581 11.0002 13.8334 8.72349 13.8334H5.11619ZM6.23239 7.60195H7.83645C9.02657 7.60195 9.70663 7.07712 9.70663 6.1753C9.70663 5.31782 9.10788 4.82995 8.0656 4.82995H6.23239V7.60195ZM6.23239 12.1702H8.15431C9.44052 12.1702 10.1354 11.6232 10.1354 10.6031C10.1354 9.60519 9.41834 9.07296 8.10256 9.07296H6.23239V12.1702Z" fill="currentColor"></path>
																			</svg>
																		</button>
																		<button type="button" aria-label="Italic" class="flex h-full items-center gap-1 rounded-lg px-2.5 hover:bg-[#f5f5f5] disabled:opacity-50 disabled:cursor-not-allowed dark:hover:bg-token-main-surface-secondary disabled:hover:bg-transparent" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">
																			<svg width="16" height="17" viewBox="0 0 16 17" fill="none"
																				xmlns="http://www.w3.org/2000/svg" class="icon-sm text-token-text-primary">
																				<path d="M9.94587 13.3511C9.89814 13.6297 9.6566 13.8334 9.37393 13.8334H4.95078C4.59259 13.8334 4.31994 13.5121 4.37824 13.1587C4.42447 12.8785 4.66675 12.6729 4.95077 12.6729H6.60855L8.09599 4.32729H6.62967C6.27148 4.32729 5.99883 4.00598 6.05714 3.65257C6.10337 3.37234 6.34565 3.16675 6.62967 3.16675H11.054C11.4108 3.16675 11.683 3.4856 11.6271 3.83793C11.5824 4.11979 11.3394 4.32729 11.054 4.32729H9.39198L7.90454 12.6729H9.37393C9.73357 12.6729 10.0066 12.9967 9.94587 13.3511Z" fill="currentColor"></path>
																			</svg>
																		</button>
																		<button type="button" aria-label="Transform" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r6n:" data-state="closed" class="flex h-full items-center gap-1 rounded-lg px-2.5 hover:bg-[#f5f5f5] disabled:opacity-50 disabled:cursor-not-allowed dark:hover:bg-token-main-surface-secondary disabled:hover:bg-transparent" tabindex="-1" data-orientation="horizontal" data-radix-collection-item="">
																			<svg width="16" height="17" viewBox="0 0 16 17" fill="none"
																				xmlns="http://www.w3.org/2000/svg" class="icon-sm text-token-text-primary">
																				<path d="M12.0464 13.9622C10.5481 13.9622 9.49341 13.0267 9.49341 11.6453C9.49341 10.3004 10.5262 9.47447 12.3373 9.37214L14.4394 9.24789V8.65586C14.4394 7.80071 13.8648 7.28907 12.9047 7.28907C12.1482 7.28907 11.6464 7.55951 11.2099 8.26117C11.0499 8.49506 10.8463 8.59739 10.5699 8.59739C10.1771 8.59739 9.89345 8.33426 9.89345 7.93958C9.89345 7.77878 9.93709 7.60336 10.0316 7.42794C10.4317 6.55817 11.5882 6.00269 12.9629 6.00269C14.8176 6.00269 16.0032 6.9894 16.0032 8.53161V13.1728C16.0032 13.6698 15.6904 13.9695 15.2467 13.9695C14.8103 13.9695 14.5121 13.6845 14.4976 13.2167V12.5662H14.4612C14.0175 13.4213 13.0429 13.9622 12.0464 13.9622ZM12.4755 12.7124C13.5738 12.7124 14.4394 11.9522 14.4394 10.9509V10.3442L12.5483 10.4612C11.61 10.527 11.079 10.9436 11.079 11.6014C11.079 12.2738 11.6391 12.7124 12.4755 12.7124Z" fill="currentColor"></path>
																				<path d="M0.814628 13.9476C0.327306 13.9476 0 13.6479 0 13.202C0 13.0778 0.0290939 12.917 0.101828 12.7196L3.29488 4.0219C3.50581 3.43718 3.86221 3.16675 4.43681 3.16675C5.00414 3.16675 5.35327 3.42987 5.57147 4.01459L8.7718 12.7196C8.84453 12.9243 8.87362 13.0632 8.87362 13.202C8.87362 13.6333 8.53177 13.9476 8.059 13.9476C7.62259 13.9476 7.38256 13.7429 7.2371 13.2751L6.43701 11.002H2.42206L1.62926 13.2678C1.47651 13.7429 1.23649 13.9476 0.814628 13.9476ZM2.83665 9.66447H6.02243L4.44409 5.03786H4.40044L2.83665 9.66447Z" fill="currentColor"></path>
																			</svg>
																		</button>
																	</div>
																</div>
															</div>
															<div class="pointer-events-none relative flex h-full flex-shrink-0 z-20 basis-0" style="width: 0px; opacity: 1; will-change: auto;">
																<div class="pointer-events-auto absolute bottom-0 left-0 top-0 w-0 overflow-visible pl-2"></div>
															</div>
														</div>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
							</main>
