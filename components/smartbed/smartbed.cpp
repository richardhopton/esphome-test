#include "smartbed.h"
#include "esphome/core/log.h"

namespace esphome
{
    namespace smartbed
    {
        static const char *TAG = "smartbed";

        void Smartbed::dump_config()
        {
            ESP_LOGCONFIG(TAG, "Smartbed:");
            LOG_SWITCH("  ", "Safety Light Switch", this->safety_light_switch_);
            this->check_uart_settings(38400, 2, uart::UART_CONFIG_PARITY_EVEN, 8);
        }

        void Smartbed::loop()
        {

        }

        void SmartbedSwitch::write_state(bool state)
        {
            this->parent_->send_command(this->command_, this->command_count_);
        }

        void SmartbedButton::press_action()
        {
            this->parent_->send_command(this->command_, this->command_count_);
        }
    }
}
