/*
 * SPDX-FileCopyrightText: 2023 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Unlicense OR CC0-1.0
 */

#pragma once
#include "esp_pm.h"
#include "esp_check.h"
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/queue.h"

/* pm lock type */
#if (CONFIG_EXAMPLE_PM_LOCK_TYPE == 0)
#define DEFAULT_PM_LOCK_TYPE	(ESP_PM_CPU_FREQ_MAX)
#elif (CONFIG_EXAMPLE_PM_LOCK_TYPE == 1)
#define DEFAULT_PM_LOCK_TYPE	(ESP_PM_APB_FREQ_MAX)
#else
#define DEFAULT_PM_LOCK_TYPE	(ESP_PM_NO_LIGHT_SLEEP)
#endif

/* easy to print lock type */
#define PM_LOCK_TYPE_TO_STRING	(DEFAULT_PM_LOCK_TYPE == 0 ? "CPU_FREQ_MAX" : (DEFAULT_PM_LOCK_TYPE == 1 ? "APB_FREQ_MAX" : "NO_LIGHT_SLEEP"))


/* system hold lock state */
typedef enum{
	NO_LOCK_STATE = 0,
	HOLD_LOCK_STATE = 1
} hold_pm_lock_state_t;


#ifdef __cplusplus
extern "C" {
#endif

esp_err_t example_register_power_config( void* );

#ifdef __cplusplus
}
#endif
