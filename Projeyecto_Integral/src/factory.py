from marshmallow import Schema, fields, ValidationError, validates
from .cliente import Cliente
from .domicilio import Domicilio
from .datos_personales import DatosPersonales

class ClienteFactory:
    @staticmethod
    def validar_datos_json(datos_json, domicilios_json):
        class DatosJsonSchema(Schema):
            firstName = fields.Str(required=True)
            lastName = fields.Str(required=True)
            userEmail = fields.Email(required=True)
            gender = fields.Str(required=True)
            userNumber = fields.Str(required=True)
            dateOfBirthInput = fields.Str(required=True)
            subjects = fields.List(fields.Str(), required=True)
            hobbies = fields.List(fields.Str(), required=True)
            state = fields.Str(required=True)
            city = fields.Str(required=True)

            @validates("subjects")
            def validate_subjects(self, value):
                allowed_subjects = {"English", "Maths", "Physics", "Social Stuides", "Chemistry", "Accounting",
                                    "Arts", "Computer Science", "Commerce", "Economics", "Civics", "Biology", "Hindi", "History"}
                for subject in value:
                    if subject not in allowed_subjects:
                        raise ValidationError(f"Invalid subject: {subject}")

            @validates("gender")
            def validate_gender(self, value):
                allowed_gender = {"male", "female", "other"}
                if value.lower() not in allowed_gender:
                    raise ValidationError("Invalid gender. Must be 'male', 'female', or 'other'.")

            @validates("state")
            def validate_state(self, value):
                allowed_states = {"NCR", "Uttar", "Haryana", "Rajastha"}
                if value not in allowed_states:
                    raise ValidationError("Invalid state.")

            @validates("city")
            def validate_city(self, value):
                state = self.context.get("state", "").lower()
                allowed_cities = {
                    "ncr": {"delhi", "gurgaon", "noida"},
                    "uttar": {"agra", "lucknow", "merrut"},
                    "haryana": {"karnal", "panipat"},
                    "rajastha": {"jaipur", "jaiselmer"}
                }
                if value.lower() not in allowed_cities.get(state, set()):
                    raise ValidationError(f"Invalid city ({value}) for the specified {state}.")

            @validates("hobbies")
            def validate_hobbies(self, value):
                allowed_hobbies = {"sports", "reading", "music"}
                for hobby in value:
                    if hobby.lower() not in allowed_hobbies:
                        raise ValidationError(f"Invalid hobby: {hobby}")



        class DomiciliosJsonSchema(Schema):
            currentAddress = fields.Str(required=None)
            permanentAddress = fields.Str(required=None)


        try:
            # DatosJsonSchema().load(datos_json)
            DatosJsonSchema(context={"state": datos_json.get("state", "")}).load(datos_json)

            for domicilio in domicilios_json:
                DomiciliosJsonSchema().load(domicilio)
        except ValidationError as e:
            raise ValidationError(f"Error de validación JSON: {e}")

    @staticmethod
    def crear_cliente(datos_json: dict, domicilios_json: dict):
        ClienteFactory.validar_datos_json(datos_json, domicilios_json)

        datos_personales = DatosPersonales(
            datos_json["firstName"],
            datos_json["lastName"],
            datos_json["userEmail"],
            datos_json["gender"],
            datos_json["userNumber"],
            datos_json["dateOfBirthInput"],
            datos_json["subjects"],
            datos_json["hobbies"],
            datos_json["state"],
            datos_json["city"]
        )

        domicilios = []
        for domicilio_data in domicilios_json:
            if "currentAddress" in domicilio_data:
                domicilios.append(Domicilio(domicilio_data["currentAddress"], is_shipping=True))
            elif "permanentAddress" in domicilio_data:
                domicilios.append(Domicilio(domicilio_data["permanentAddress"]))

        return Cliente(datos_personales, domicilios)
