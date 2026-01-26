from argparse import Namespace

import cv2
import pygame
import argparse


def convert_frame_to_ascii(frame, width=100):

    ascii_chars = " .:;+=*#@MW$" # for medium grade detailing using ASCII

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


def play_video_in_pygame(video_path, audio_path, char_width, font_size):

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
    pygame.display.set_caption("Real time ASCII Video Player")


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


def load_arguments_from_cli() -> Namespace | None :
    """
    Returns expected arguments

    :return:
    """
    DEFAULT_CHAR_WIDTH = 100
    DEFAULT_VIDEO_PATH = "sample/video.mp4"
    DEFAULT_AUDIO_PATH = None
    DEFAULT_FONT_SIZE = 10

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", type=str, default=DEFAULT_VIDEO_PATH , help="Input video file path")
    parser.add_argument("-a", type=str, default=DEFAULT_AUDIO_PATH , help="Audio file path (do not use it for no audio)")
    parser.add_argument("--char-width", type=str, default=DEFAULT_CHAR_WIDTH, help="ASCII output width (detail level)")
    parser.add_argument("--font-size", type=str, default=DEFAULT_FONT_SIZE, help="Rendering font size")

    return parser.parse_args()


if __name__ == "__main__":
    args = load_arguments_from_cli()
    video_path = args.v
    audio_path = args.a
    char_width = args.char_width
    font_size = args.font_size


    print(f"Loading video: {video_path}")
    if audio_path:
        print(f"Loading separate audio: {audio_path}")
    else:
        print("No audio will be played")

    play_video_in_pygame(video_path, audio_path, char_width, font_size)
