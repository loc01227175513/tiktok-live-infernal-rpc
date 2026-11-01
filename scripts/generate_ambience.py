from pathlib import Path
import wave, math, struct
out=Path(__file__).resolve().parents[1]/'public/assets/infernal_ambience.wav'
rate=22050;duration=16
with wave.open(str(out),'wb') as f:
 f.setparams((1,2,rate,0,'NONE','not compressed'))
 for i in range(rate*duration):
  t=i/rate;env=math.sin(math.pi*t/duration)**2
  v=sum(math.sin(2*math.pi*hz*t)+.15*math.sin(4*math.pi*hz*t) for hz in [65.4064,77.7817,97.9989])/3
  f.writeframesraw(struct.pack('<h',round(v*env*2200)))
