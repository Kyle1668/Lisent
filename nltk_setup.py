"""
  This is needed to install necessary dependencies for NLTK.
  Ran upon Docker build.
"""

import nltk
nltk.download('punkt')
