# SPDX-FileCopyrightText: 2023 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import logging
import time

import pytest
from pytest_embedded import Dut

CONFIGS = [
    pytest.param('low_level_control_esp32c6', marks=[pytest.mark.esp32c6]),
    pytest.param('low_level_control_esp32s3', marks=[pytest.mark.esp32s3])
]


@pytest.mark.generic
@pytest.mark.parametrize('config', CONFIGS, indirect=True)
def test_low_level_control(dut: Dut) -> None:

    RELEASE_STR = r'Release (\w+) lock finished, system may sleep'
    ACQUIRE_STR = r'Acquire (\w+) lock finished, can to do something'

    dut.serial.proc.setDTR(False)
    dut.serial.proc.setRTS(False)
    dut.serial.proc.setDTR(True)

    # while True:
    #     dut.serial.proc.setDTR(True)
    #     time.sleep(2)
    #     dut.serial.proc.setDTR(False)
    #     time.sleep(1)

    dut.serial.proc.setDTR(False)  # 对应设置GPIO 0高
    dut.expect(RELEASE_STR)
    time.sleep(1)
    dut.serial.proc.setDTR(True)  # 对应设置GPIO 0低
    dut.expect(ACQUIRE_STR)
    time.sleep(1)
    dut.serial.proc.setDTR(False)
    dut.expect(RELEASE_STR)

    time.sleep(10)
    dut.write('U')
    time.sleep(1)
    dut.expect(ACQUIRE_STR)
    logging.info('Wakeup by UART')
    dut.expect(RELEASE_STR)
