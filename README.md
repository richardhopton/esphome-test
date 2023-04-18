# Smartbed component

ESPHome custom external components for interfacing with Smartbeds

## How to use:-

```yaml
external_components:
    - source:
          type: git
          url: https://github.com/richardhopton/esphome-test
      components: [smartbed]

uart:
    - id: smartbed_uart
      tx_pin: 13
      rx_pin: 16
      baud_rate: 38400
      parity: EVEN
      stop_bits: 2
      half_duplex: true

smartbed:
    uart_id: smartbed_uart
    safety_light_switch:
        name: Safety Light
    head_angle_sensor:
        name: Head Angle
    foot_angle_sensor:
        name: Foot Angle
    massage_mode_button:
        name: Massage Mode
```
