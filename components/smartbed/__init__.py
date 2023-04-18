import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import button, sensor, switch, uart
from esphome.const import (
    CONF_ID,
    STATE_CLASS_MEASUREMENT,
    UNIT_DEGREES,
)

MULTI_CONF = True
DEPENDENCIES = ['uart']
AUTO_LOAD = ['switch']

smartbed_ns = cg.esphome_ns.namespace('smartbed')
Smartbed = smartbed_ns.class_('Smartbed', uart.UARTDevice, cg.PollingComponent)
SmartbedSwitch = smartbed_ns.class_("SmartbedSwitch", switch.Switch, cg.Component)
SmartbedButton = smartbed_ns.class_("SmartbedButton", button.Button, cg.Component)

CONF_SAFETY_LIGHT_SWITCH = "safety_light_switch"
CONF_MASSAGE_MODE_BUTTON = "massage_mode_button"
CONF_HEAD_ANGLE_SENSOR = "head_angle_sensor"
CONF_FOOT_ANGLE_SENSOR = "foot_angle_sensor"

CONFIG_SCHEMA = uart.UART_DEVICE_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Smartbed),
    cv.Optional(CONF_SAFETY_LIGHT_SWITCH): switch.switch_schema(SmartbedSwitch),
    cv.Optional(CONF_MASSAGE_MODE_BUTTON): button.button_schema(SmartbedButton),
    cv.Optional(CONF_HEAD_ANGLE_SENSOR): sensor.sensor_schema(
        unit_of_measurement=UNIT_DEGREES,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_FOOT_ANGLE_SENSOR): sensor.sensor_schema(
        unit_of_measurement=UNIT_DEGREES,
        accuracy_decimals=0,
        state_class=STATE_CLASS_MEASUREMENT,
    )
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_SAFETY_LIGHT_SWITCH in config:
        safety_light_switch = await switch.new_switch(config[CONF_SAFETY_LIGHT_SWITCH])
        cg.add(safety_light_switch.set_parent(var))
        cg.add(safety_light_switch.set_command('safety_lights'))
        cg.add(var.set_safety_light_switch(safety_light_switch))

    if CONF_MASSAGE_MODE_BUTTON in config:
        massage_mode_button = await button.new_button(config[CONF_MASSAGE_MODE_BUTTON])
        cg.add(massage_mode_button.set_parent(var))
        cg.add(massage_mode_button.set_command('massage_mode'))

    if CONF_HEAD_ANGLE_SENSOR in config:
        head_angle_sensor = await sensor.new_sensor(config[CONF_HEAD_ANGLE_SENSOR])
        cg.add(var.set_head_angle_sensor(head_angle_sensor))

    if CONF_FOOT_ANGLE_SENSOR in config:
        foot_angle_sensor = await sensor.new_sensor(config[CONF_FOOT_ANGLE_SENSOR])
        cg.add(var.set_foot_angle_sensor(foot_angle_sensor))
