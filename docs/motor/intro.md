# Motor

Interface for TB6600 motor drive

"This is a professional two-phase stepper motor driver. It supports speed and direction control. You can set its micro step and output current with 6 DIP switch. There are 7 kinds of micro steps (1, 2 / A, 2 / B, 4, 8, 16, 32) and 8 kinds of current control (0.5A, 1A, 1.5A, 2A, 2.5A, 2.8A, 3.0A, 3.5A) in all. And all signal terminals adopt high-speed optocoupler isolation, enhancing its anti-high-frequency interference ability."

This driver works by pulsing a signal on and off(50% on, 50% off) with a frequency of up to 13 KHz. To run the motor drivers at a higher frequency, the motor driver needs higher voltages. So to run at 13 KHz, the driver needs up to 40V.

```{note}
Maximum pulse frequency of 13 KHz. To use higher frequencies and speeds, the driver needs higher voltages.
```

## Datasheet
[DFROBOT](https://dfimg.dfrobot.com/nobody/wiki/0bcc0b661ce7750ff7d0134bfc3e88b3.pdf)

## DIP-switch configuration

### Microstep control

Microstep determines the step angle of the driver/motor configuration. 

Stepper motors have a step angle which specifies what angle each step is. The microstep determines how much this step will be split up.
The resulting step angle can be calculated in the following formula.

\begin{gather*}
Angle\: per\: step = \frac{Motor\: angle}{Microstep} 
\end{gather*}

<style>
  table {
    border-collapse: collapse;
    width: 100%;
    color: var(--color-content-foreground);
    font-family: Arial, sans-serif;
    font-size: 14px;
    text-align: left;
    border-radius: 5px;
    overflow: hidden;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    margin: auto;
    margin-top: 50px;
    margin-bottom: 50px;
  }
table th {
  background-color: var(--color-api-name);
  color: #fff;
  font-weight: bold;
  padding: 1px;
  text-transform: uppercase;
  letter-spacing: 1px;
  } 

table tr:hover td {
  background-color: var(--color-link);
  opacity: 90%;
}
</style>

<table class="styled-table">
  <thead>
    <tr>
      <th>Micro Step</th>
      <th>Pulse/Rev</th>
      <th>S1</th>
      <th>S2</th>
      <th>S3</th>
    </tr>
  </thead>
  <tbody>
    <tr class="active-row">
      <td>NC</td>
      <td>NC</td>
      <td>ON</td>
      <td>ON</td>
      <td>ON</td>
    </tr>
    <tr class="active-row">
      <td>1</td>
      <td>200</td>
      <td>ON</td>
      <td>ON</td>
      <td>OFF</td>
    </tr>
    <tr class="active-row">
      <td>2/A</td>
      <td>400</td>
      <td>ON</td>
      <td>OFF</td>
      <td>ON</td>
    </tr>
    <tr class="active-row">
      <td>2/B</td>
      <td>400</td>
      <td>OFF</td>
      <td>ON</td>
      <td>ON</td>
    </tr>
    <tr class="active-row">
      <td>4</td>
      <td>800</td>
      <td>ON</td>
      <td>OFF</td>
      <td>OFF</td>
    </tr>
    <tr class="active-row">
      <td>8</td>
      <td>1600</td>
      <td>OFF</td>
      <td>ON</td>
      <td>OFF</td>
    </tr>
    <tr class="active-row">
      <td>16</td>
      <td>3200</td>
      <td>OFF</td>
      <td>OFF</td>
      <td>ON</td>
    </tr>
    <tr class="active-row">
      <td>32</td>
      <td>6400</td>
      <td>OFF</td>
      <td>OFF</td>
      <td>OFF</td>
    </tr>
  </tbody>
</table>

### Current control
<table class="styled-table">
  <tr class="active-row">
    <th>Current (A)</th>
    <th>PK Current (A)</th>
    <th>S4</th>
    <th>S5</th>
    <th>S6</th>
  </tr>
  <tr class="active-row">
    <td>0.5</td>
    <td>0.7</td>
    <td>ON</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr class="active-row">
    <td>1.0</td>
    <td>1.2</td>
    <td>ON</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr class="active-row">
    <td>1.5</td>
    <td>1.7</td>
    <td>ON</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr class="active-row">
    <td>2.0</td>
    <td>2.2</td>
    <td>ON</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
  <tr class="active-row">
    <td>2.5</td>
    <td>2.7</td>
    <td>OFF</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr class="active-row">
    <td>2.8</td>
    <td>2.9</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr class="active-row">
    <td>3.0</td>
    <td>3.2</td>
    <td>OFF</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr class="active-row">
    <td>3.5</td>
    <td>4.0</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
</table>

## Wiring
```{image} Motor-kobling.png
```
