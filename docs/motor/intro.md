# motor

## Datasheet
[DFROBOT](https://dfimg.dfrobot.com/nobody/wiki/0bcc0b661ce7750ff7d0134bfc3e88b3.pdf)

## DIP-switch configuration

### Step control

<table border="1"  
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15) >
  <tr>
    <th>Micro Step</th>
    <th>Pulse/Rev</th>
    <th>S1</th>
    <th>S2</th>
    <th>S3</th>
  </tr>
   <tr>
    <td>NC</td>
    <td>NC</td>
    <td>ON</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>1</td>
    <td>200</td>
    <td>ON</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>2/A</td>
    <td>400</td>
    <td>ON</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>2/B</td>
    <td>400</td>
    <td>OFF</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>4</td>
    <td>800</td>
    <td>ON</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>8</td>
    <td>1600</td>
    <td>OFF</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>16</td>
    <td>3200</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>32</td>
    <td>6400</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
</table>

### Current control
<table border="1">
  <tr>
    <th>Current (A)</th>
    <th>PK Current (A)</th>
    <th>S4</th>
    <th>S5</th>
    <th>S6</th>
  </tr>
  <tr>
    <td>0.5</td>
    <td>0.7</td>
    <td>ON</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>1.0</td>
    <td>1.2</td>
    <td>ON</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>1.5</td>
    <td>1.7</td>
    <td>ON</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>2.0</td>
    <td>2.2</td>
    <td>ON</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>2.5</td>
    <td>2.7</td>
    <td>OFF</td>
    <td>ON</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>2.8</td>
    <td>2.9</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>ON</td>
  </tr>
  <tr>
    <td>3.0</td>
    <td>3.2</td>
    <td>OFF</td>
    <td>ON</td>
    <td>OFF</td>
  </tr>
  <tr>
    <td>3.5</td>
    <td>4.0</td>
    <td>OFF</td>
    <td>OFF</td>
    <td>OFF</td>
  </tr>
</table>

