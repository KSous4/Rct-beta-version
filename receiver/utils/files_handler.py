from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET


class Filemanager:
    def __init__(self):
        pass

    @staticmethod
    def parse_response(data: dict) -> str:

        xml_result = dicttoxml(data, custom_root='CorrectTransit', attr_type=False)

        root = ET.fromstring(xml_result)

        envelope = ET.Element(
            'soap:Envelope',
            xmlns_soap="http://schemas.xmlsoap.org/soap/envelope/",
            xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
            xmlns_xsd="http://www.w3.org/2001/XMLSchema",
        )

        body = ET.SubElement(envelope, 'soap:Body')

        correct_transit = ET.Element(
            'CorrectTransit',
            xmlns="urn:www.softinsa.pt:mz.arteris.CMServer"
        )

        correct_transit.append(root)

        body.append(correct_transit)

        xml_string = ET.tostring(envelope, encoding='utf-8').decode('utf-8')
        return xml_string

    @staticmethod
    def get_data_to_inference(data: dict):
        values: dict = {
            'id': data['transit']['passage']['transactionId'],
            'cat_dac': data['transit']['passage']['passageClass']['tollClass'],
            'cat_cla': data['transit']['passage']['collector']['collectorTollClass']['tollClass']
        }

        return values
