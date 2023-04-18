#pragma once

#include "esphome/core/component.h"
#include "esphome/components/button/button.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/switch/switch.h"
#include "esphome/components/uart/uart.h"

namespace esphome
{
    namespace smartbed
    {
        class Smartbed : public Component, public uart::UARTDevice
        {
        public:
            void set_safety_light_switch(switch_::Switch *safety_light_switch) { safety_light_switch_ = safety_light_switch; }
            void set_head_angle_sensor(sensor::Sensor *head_angle_sensor) { head_angle_sensor_ = head_angle_sensor; }
            void set_foot_angle_sensor(sensor::Sensor *foot_angle_sensor) { foot_angle_sensor_ = foot_angle_sensor; }
            void send_command(std::string command, int count)
            {
                this->command_ = command;
                this->command_count_ = count;
            }
            void dump_config() override;
            void loop() override;

        protected:
            switch_::Switch *safety_light_switch_{nullptr};
            sensor::Sensor *head_angle_sensor_{nullptr};
            sensor::Sensor *foot_angle_sensor_{nullptr};

            std::string command_;
            int command_count_;
        };

        class SmartbedSwitch : public switch_::Switch
        {
        public:
            void set_parent(Smartbed *parent) { this->parent_ = parent; }
            void set_command(std::string command, int count = 5)
            {
                this->command_ = command;
                this->command_count_ = count;
            }

        protected:
            void write_state(bool state) override;

            Smartbed *parent_;
            std::string command_;
            int command_count_;
        };

        class SmartbedButton : public button::Button
        {
        public:
            void set_parent(Smartbed *parent) { this->parent_ = parent; }
            void set_command(std::string command, int count = 5)
            {
                this->command_ = command;
                this->command_count_ = count;
            }

        protected:
            void press_action() override;

            Smartbed *parent_;
            std::string command_;
            int command_count_;
        };

    }
}
