import cv2
import pygame
import numpy as np


def convert_frame_to_ascii(frame, width=100):

    ascii_chars = " .:;+=*#@MW$"

    height = int(frame.shape[0] * width / frame.shape[1] / 2)
    if height == 0:
        height = 1

    resized_frame = cv2.resize(frame, (width, height))

    if len(resized_frame.shape) > 2:
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    else:
        gray_frame = resized_frame

    normalized = gray_frame / 255.0
    ascii_frame = []

    for row in normalized:
        line = ""
        for pixel in row:
            index = int(pixel * (len(ascii_chars) - 1))
            line += ascii_chars[index]
        ascii_frame.append(line)

    return ascii_frame


def play_video_in_pygame(video_path, audio_path=None, char_width=100, font_size=12):

    # audio
    pygame.init()
    pygame.mixer.init()

    # video
    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if video_fps == 0:
        video_fps = 30

    # display
    char_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * char_width / cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
    window_width = char_width * (font_size // 4 + 4)
    window_height = char_height * font_size
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Rehaman Dakait")


    try:
        font = pygame.font.SysFont('couriernew', font_size)
    except:
        font = pygame.font.Font(pygame.font.get_default_font(), font_size)

    if audio_path:
        try:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
            print(f"Audio loaded and playing from: {audio_path}")
        except Exception as e:
            print(f"Could not load audio: {e}")
    else:
        print("No audio file specified - playing video without audio")

    clock = pygame.time.Clock()
    running = True
    frame_count = 0

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        # Pause/unpause
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

            ret, frame = cap.read()
            if not ret:
                print("Video finished")
                break

            ascii_lines = convert_frame_to_ascii(frame, char_width)

            #background
            screen.fill((0, 0, 0))

            # Render
            y_pos = 5
            for line in ascii_lines:
                text_surface = font.render(line, True, (200, 255, 200))
                screen.blit(text_surface, (5, y_pos))
                y_pos += font_size

            pygame.display.flip()
            clock.tick(video_fps)
            frame_count += 1

    except KeyboardInterrupt:
        print("\nPlayback interrupted")
    except Exception as e:
        print(f"Error during playback: {e}")

    finally:
        cap.release()
        pygame.mixer.music.stop()
        pygame.quit()
        print(f"Played {frame_count} frames")


if __name__ == "__main__":
    VIDEO_PATH = "vid6.mp4"
    AUDIO_PATH = "1.mp3"
    CHAR_WIDTH = 100
    FONT_SIZE = 10


    print(f"Loading video: {VIDEO_PATH}")
    if AUDIO_PATH:
        print(f"Loading separate audio: {AUDIO_PATH}")
    else:
        print("No audio will be played")

    play_video_in_pygame(VIDEO_PATH, AUDIO_PATH, CHAR_WIDTH, FONT_SIZE)