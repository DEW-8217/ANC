피코 데스크톱 됬던거
from machine import I2S, Pin
import array
import time

# I2S 설정 값
SAMPLE_RATE = 16000       # 16kHz
SAMPLE_BITS = 16          # 16-bit samples
BUFFER_LENGTH = 1024      # 한번에 읽을 샘플 수

# I2S 초기화
audio_in = I2S(
    0,
    sck=Pin(18),     # BCLK
    ws=Pin(19),      # LRCLK
    sd=Pin(20),      # DOUT (I2S data)
    mode=I2S.RX,
    bits=SAMPLE_BITS,
    format=I2S.MONO,
    rate=SAMPLE_RATE,
    ibuf=BUFFER_LENGTH * 2
)

# 샘플 저장할 버퍼
samples = array.array('h', [0] * BUFFER_LENGTH)

print("I2S 마이크에서 오디오 샘플 읽기 시작!")

while True:
    # I2S로부터 샘플 읽기
    num_read = audio_in.readinto(samples)

    if num_read > 0:
        # 예: 첫 5개 샘플 출력
        print("Samples:", samples[:5])
    
    time.sleep(0.1)
