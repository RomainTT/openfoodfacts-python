#/usr/bin/env python
# -*- coding: utf-8 -*-

"""openfoodfacts objects to communicate with "Product Opener" servers."""

import requests

from openfoodfacts.logger import get_logger


# ------------------------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------------------------

# This constant describes the different file formats that can be downloaded
# from the servers.
FILE_TYPE_MAP = {
    "mongodb": "openfoodfacts-mongodbdump.tar.gz",
    "csv": "en.openfoodfacts.org.products.csv",
    "rdf": "en.openfoodfacts.org.products.rdf"
}

URL_MAP = {
    "food": "https://%s.openfoodfacts.org/",
    "beauty": "https://%s.openbeautyfacts.org/",
    "pet": "https://%s.openpetfoodfacts.org/"
}

SUBDOMAIN_MAP = {
    "api": "ssl-api",
}


# ------------------------------------------------------------------------------
# CLASSES
# ------------------------------------------------------------------------------

class Client(object):
    """Client object enable to send requests to the server."""

    def __init__(self, product_type="food", username=None, password=None,
                 url=None):
        """Initialization of a Client object.

        Args:
            product_type: (str) (optional) Product type to target the right
                server. Whether "food", "beauty", or "pet". This can be
                overriden by the argument "url" if you want to give your custom
                full URL to the server.
            username: (str) (optional) username to identify on the server.
                Required for write operations.
            password: (str) (optional) password to identify on the server.
                Required for write operations.
            url: (str) (optional) used to override the defaults URLs used in
                function of the argument "product_type". Must be a URL pointing
                to a valid server, and the string must contain a "{}" as
                sub-domain in order to insert subdomain dynamically.
        """
        self._logger = get_logger(self.__class__.__name__)

        # Save the base url
        if url:
            self.base_url = url
        elif product_type in URL_MAP.keys():
            self.base_url = URL_MAP[product_type]
        else:
            raise ValueError("product_type has an unknown value.")

        # Create session
        self.session = requests.session()

        # Login to the server if necessary
        if (username or password) and not (username and password):
            raise ValueError("Please provide both username AND password.")
        elif username:
            self.session.

    def __del__(self):
        # Make sure to close the session when this object is deleted.
        self.session.close()
