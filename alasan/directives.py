class Dialog:
    @staticmethod
    def delegate(intent_name=None, updated_intent={}):
        return {
            "type": "Dialog.Delegate",
            "updatedIntent": updated_intent
        }

    @staticmethod
    def elicit_slot(slot_to_elicit, updated_intent={}):
        return {
            "type": "Dialog.Elicit",
            "slotToElicit": slot_to_elicit,
            "updatedIntent": updated_intent
        }

    @staticmethod
    def confirm_slot(slot_to_confirm, updated_intent={}):
        return {
            "type": "Dialog.ConfirmSlot",
            "slotToElicit": slot_to_confirm,
            "updatedIntent": updated_intent
        }

    @staticmethod
    def confirm_intent(updated_intent={}):
        return {
            "type": "Dialog.ConfirmIntent",
            "updatedIntent": updated_intent
        }
