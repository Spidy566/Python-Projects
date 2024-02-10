import ffmpeg
import os


def video_compress(file, cr):
    input_file = file
    output_file = os.path.splitext(input_file)[0] + '_compressed.mp4'
    cr = int(cr) if cr else 26
    (
        ffmpeg.input(input_file)
        .output(output_file, crf=cr, vcodec="libx264")
        .run()
    )
    return output_file


if __name__ == "__main__":
    video_path = input("Enter the video file path: ")
    CR = input("Compression Rate [0-51] (Default: 26):")
    video_compress(video_path, CR)
    print("Video Compressed Successfully")
