"""Code for create the fucntions that allow us to get the data of the charger."""
from __future__ import annotations

# pylint: disable=invalid-name
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Defaults

BAUD = 19200


class Charger:
    """We acces to the charger and we can get all the data we need."""

    def __init__(self, ip):
        Defaults.Timeout = 10
        self.ip = ip
        self.is_running = True
        self.demon = True
        self.data = {}
        self.client = ModbusTcpClient(
            host=self.ip, port=502, timeout=10, baudrate=BAUD, parity="N"
        )

    # To do!: Implement try/except
    def _conection(self):
        """Etablish the connection with the Modbus Client."""
        self.client.connect()

    def shutDown(self):
        """Shunting down conection."""
        self.client.close()

    def regenera_float(self, lectura):
        """Change the value to a Float(big endian):"""
        if not lectura.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(
                lectura.registers, byteorder=Endian.Big, wordorder=Endian.Big
            )
            return float("{0:.0f}".format(decoder.decode_32bit_float()))
        else:
            return None

    # To do!: Implement try/except
    def _read_register(self, command: str):
        """Read the registers of the Trydan Charger."""
        data = float(0.0)
        value = self.client.read_holding_registers(command, 2, unit=1)
        data = self.regenera_float(value)
        return data

    # To do!: Implement try/except
    def _write_register(self, command: str, data_to_write: int):
        """Write new registers to the Trydan Charger."""
        value_write = self.client.write_register(command, value=data_to_write, unit=1)
        output_flag = "Success" if value_write else "Failure"
        return print("Writing single coil status: " + output_flag)

    ### WRITE HOLDING REGISTER 0X006:

    def postPauseState(self):
        """Post the charger's pause state."""
        command = 0x0177A
        data_to_write = int(input("Write the asnwer:"))
        post_pause_state = self._write_register(command, data_to_write)
        return post_pause_state

    def postLock(self):
        """Post the charger's lock state."""
        command = 0x0177B
        data_to_write = int(input("Write the asnwer:"))
        post_lock = self._write_register(command, data_to_write)
        return post_lock

    def postPromgram(self):
        """Post the charger's promgram state."""
        command = 0x0177C
        data_to_write = int(input("Write the asnwer:"))
        post_promgram = self._write_register(command, data_to_write)
        return post_promgram

    def postIntensity(self):
        """Post the charger's intensity."""
        command = 0x0177D
        data_to_write = int(input("Write the asnwer:"))
        post_intensity = self._write_register(command, data_to_write)
        return post_intensity

    def postDynamic(self):
        """Post the charger's dynamic state."""
        command = 0x0177E
        data_to_write = int(input("Write the asnwer:"))
        post_dynamic = self._write_register(command, data_to_write)
        return post_dynamic

    def postPayment(self):
        """Post the charger's payment state."""
        command = 0x0177F
        data_to_write = int(input("Write the asnwer:"))
        post_payment = self._write_register(command, data_to_write)
        return post_payment

    def postOcpp(self):
        """Post the charger's OCPP state."""
        command = 0x01780
        data_to_write = int(input("Write the asnwer:"))
        post_ocpp = self._write_register(command, data_to_write)
        return post_ocpp

    def postMinIntensity(self):
        """Post the charger's Minimum Intensity."""
        command = 0x01781
        data_to_write = int(input("Write the asnwer:"))
        post_min_intensity = self._write_register(command, data_to_write)
        return post_min_intensity

    def postMaxIntensity(self):
        """Post the charger's Maximum intensity."""
        command = 0x01782
        data_to_write = int(input("Write the asnwer:"))
        post_max_intensity = self._write_register(command, data_to_write)
        return post_max_intensity

    def postPauseDynamic(self):
        """Post the charger's pause dynamic state."""
        command = 0x01783
        data_to_write = int(input("Write the asnwer:"))
        post_pause_dynamic = self._write_register(command, data_to_write)
        return post_pause_dynamic

    def postDynamicPowerMode(self):
        """Post the charger's Dynamic power mode."""
        command = 0x01784
        data_to_write = int(input("Write the asnwer:"))
        post_dynamic_power = self._write_register(command, data_to_write)
        return post_dynamic_power

    def postContractedPower(self):
        """Post the charger's Contracted power state."""
        command = 0x01785
        data_to_write = int(input("Write the asnwer:"))
        post_contracted_power = self._write_register(command, data_to_write)
        return post_contracted_power

    ### READ HOLDING REGISTER 0X003:

    def getChargeState(self):
        """Returns the charger's charge state."""
        command = 0x0BC2
        charger_state = self._read_register(command)
        return charger_state

    def getChargePower(self):
        """Returns the charger's charge power."""
        command = 0x0BC3
        charge_power = self._read_register(command)
        return charge_power

    def getChargeEnergy(self):
        """Returns the charger's charge energy."""
        command = 0x0BC4
        charge_energy = self._read_register(command)
        return charge_energy

    def getSlaveError(self):
        """Returns the charger's slave error."""
        command = 0x0BC5
        slave_error = self._read_register(command)
        return slave_error

    def getChargeTime(self):
        """Returns the charger's charge time."""
        command = 0x0BC6
        charge_time = self._read_register(command)
        return charge_time

    def getValuePWM(self):
        """Returns the charger's value PWM."""
        command = 0x0BC7
        value_PWM = self._read_register(command)
        return value_PWM

    def getHousePower(self):
        """Returns the charger's house power."""
        command = 0x0BC8
        house_power = self._read_register(command)
        return house_power

    def getPowerFV(self):
        """Returns the charger's power FV."""
        command = 0x0BC9
        power_FV = self._read_register(command)
        return power_FV

    def getPauseState(self):
        """Returns the charger's pause state."""
        command = 0x0BCA
        pause_state = self._read_register(command)
        return pause_state

    def getLock(self):
        """Returns the charger's lock state."""
        command = 0x0BCB
        lock_state = self._read_register(command)
        return lock_state

    def getPromgram(self):
        """Returns the charger's promgram state."""
        command = 0x0BCC
        promgram_state = self._read_register(command)
        return promgram_state

    def getIntensity(self):
        """Returns the charger's intensity state."""
        command = 0x0BCD
        intensity_state = self._read_register(command)
        return intensity_state

    def getDynamic(self):
        """Returns the charger's dynamic state."""
        command = 0x0BCE
        dynamic_state = self._read_register(command)
        return dynamic_state

    def getPayment(self):
        """Returns the charger's payment state."""
        command = 0x0BCF
        payment_state = self._read_register(command)
        return payment_state

    def getOCPP(self, ocpp_state):
        """Returns the charger's OCPP state."""
        command = 0x0BD0
        ocpp_state = self._read_register(command)
        print(ocpp_state)

    def getMinIntensity(self):
        """Returns the charger's Minimum Intensity state."""
        command = 0x0BD1
        min_intensity = self._read_register(command)
        print(min_intensity)

    def getMaxIntensity(self):
        """Returns the charger's Maximum Intensity state."""
        command = 0x0BD2
        max_intensity = self._read_register(command)
        print(max_intensity)

    def getPauseDynamic(self):
        """Returns the charger's Pause Dynamic state."""
        command = 0x0BD3
        pause_dynamic = self._read_register(command)
        print(pause_dynamic)

    def getDynamicPowerMode(self):
        """Returns the charger's Dynamic Power mode."""
        command = 0x0BD4
        dynamic_power = self._read_register(command)
        print(dynamic_power)

    def getContractedPower(self):
        """Returns the charger's Contracted Power state."""
        command = 0x0BD5
        contracted_power = self._read_register(command)
        print(contracted_power)
