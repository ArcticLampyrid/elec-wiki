# 微妙级滴答操作
## 微妙级延时函数
```c
#include "stm32f4xx_hal.h"

void delay_us(unsigned long us)
{
    volatile uint32_t currentTicks = SysTick->VAL;
    const uint32_t tickPerMs = SysTick->LOAD + 1;
    const uint32_t nbTicks = ((us - ((us > 0) ? 1 : 0)) * tickPerMs) / 1000;
    uint32_t elapsedTicks = 0;
    volatile uint32_t oldTicks = currentTicks;
    do
    {
        currentTicks = SysTick->VAL;
        elapsedTicks += (oldTicks < currentTicks) ? tickPerMs + oldTicks - currentTicks : oldTicks - currentTicks;
        oldTicks = currentTicks;
    } while (nbTicks > elapsedTicks);
}
```

原理：直接使用 SysTick 定时器的内部计数值，而不依靠 1ms 的中断触发。SysTick 定时器往往工作在较高频率，如 84MHz，因此可以用于实现微妙级的延时。

## 微妙级滴答计时
```c
#include "stm32f4xx_hal.h"

unsigned long get_tick_us()
{
    uint32_t m0 = HAL_GetTick();
    volatile uint32_t u0 = SysTick->VAL;
    uint32_t m1 = HAL_GetTick();
    volatile uint32_t u1 = SysTick->VAL;
    const uint32_t tms = SysTick->LOAD + 1;
    if (m1 != m0)
    {
        return (m1 * 1000 + ((tms - u1) * 1000) / tms);
    }
    else
    {
        return (m0 * 1000 + ((tms - u0) * 1000) / tms);
    }
}
```

原理：使用 SysTick 定时器的内部计数值计算出低于毫秒精度的部分，并结合 `HAL_GetTick` 函数的返回的毫秒计数值，计算出微妙级的计数值。  
注意：由于在调用 `HAL_GetTick` 函数和读取 `SysTick->VAL` 寄存器之间可能恰好触发 SysTick 中断并发生计数值重置，导致 1ms 的误差，因此需要读取两次，以规避这种误差（由于读取过程极快，可以认为不可能两次读取都被中断打断）。