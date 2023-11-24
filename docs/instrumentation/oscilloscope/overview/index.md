# 概述
## 简介
示波器是一种采样电压数据、显示波形图的仪器。示波器能够对随时间变化的电压信号（时变的电压信号）进行测量，然后将测量结果显示在示波器的屏幕上，以便于观察和分析。示波器的主要功能是显示电压信号的波形图。

早期的示波器多为模拟示波器，利用阴极射线管，通过水平偏置和垂直偏置系统使得打出的电子束在屏幕的荧光物质上显示，得到波形。

现代示波器多为数字示波器，利用模数转换器将模拟信号转换为数字信号，然后通过数字信号处理器进行处理，最后通过显示器显示波形。同时，大多数数字示波器还具有存储、计算、打印等功能。

## 指标
带宽、采样率和存储深度是示波器的三大技术指标。

### 带宽
示波器的带宽定义为**正弦波**信号衰减 3dB （衰减至原值的 70.7%） 时的信号频率：示波器内部的放大器对信号的放大倍数随着频率的增加而逐渐减小（可以认为有一个 RC 低通滤波器），当频率增加到一定值时，放大倍数减小到原值的 70.7%，这个频率就是示波器的带宽。示波器的带宽越大，就可以测量更加高频的信号。  

对于方波信号，根据傅里叶级数展开，方波信号可以看作是无穷多个正弦波信号的叠加。

$$
f(t)=\frac{2 E}{\pi}\left(\sin \omega_0 t+\frac{1}{3} \sin 3 \omega_0 t+\frac{1}{5} \sin 5 \omega_0 t+\cdots+\frac{1}{n} \sin n \omega_0 t+\cdots\right)
$$

为了在视觉上得到一个较为合理的方波图案，一般要求示波器的带宽是方波信号频率的 3 ~ 5 倍。

### 采样率
在利用数字方式显示模拟信号时，必须把连续的模拟信号，通过采样得到一个一个离散的、分立的点。示波器的采样率定义为示波器每秒采样的次数，这个值越大，示波器对信号的采样越精细，对信号的还原越准确。

### 存储深度
示波器的存储深度定义为示波器能够存储的波形点数，存储深度=采样率×观测时间。