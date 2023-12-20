# SysTick 入门
## 介绍
SysTick 定时器被放在了 Cortex-M 内核中，它是一个 24 位的递减计数器，可以用来产生定时中断或者作为延时计数器。

在 STM32 中，SysTick 定时器的时钟源可以是内核时钟（HCLK）或者内核时钟的 8 分频（HCLK/8）。

## HAL 库中基于 SysTick 的函数
HAL 库中的 `HAL_GetTick` 函数和 `HAL_Delay` 函数是基于 SysTick 定时器实现的，此外各种 HAL 库函数的超时（`Timeout`）参数也是基于 SysTick 定时器实现的。  

```c
// 返回自系统启动以来的所经过的时间，单位为毫秒（ms）
uint32_t HAL_GetTick(void);

// 延时指定的时间，单位为毫秒（ms）
void HAL_Delay(uint32_t Delay);
```

## 计时原理
单片机中的一切计时操作，本质上是计数操作。每个计时器都有一个计数器，随着一个恒定频率的时钟信号的到来，计数器的值不断地增加或减小，当计数器的值达到某个特定的值时，就会产生一个中断或者触发一个事件，并进行重置等操作。

SysTick 定时器的计数值是一个 24 位的寄存器，每遇到时钟信号时：

- 当计数值为 0 时，会产生一个中断或者触发一个事件，并进行重置，重置为「重装载值（Reload）」。
- 否则，令计数值减 1。


不难算出，中断的触发周期为：
$$
T = \frac{1}{f_{clock}} \times (\text{Reload} + 1)
$$

## HAL 库中的配置
在 HAL 库中，SysTick 定时器通常以 HCLK 为基准，并被默认初始化为 1ms 一次的中断，时钟源为内核时钟（HCLK）。

例如，假设 HCLK 为 84MHz，那么只要设置 SysTick 定时器的重装载值为 84000-1，于是每隔 1ms 就会产生一个中断。

CubeMX 通常将生成类似如下代码：
```c
volatile uint32_t uwTick;
void SysTick_Handler(void)
{
    // 响应 SysTick 中断
    uwTick++;
}
```

于是，`HAL_GetTick` 函数就可以这样实现：
```c
uint32_t HAL_GetTick(void)
{
    // 单位为 ms
    return uwTick;
}
```
