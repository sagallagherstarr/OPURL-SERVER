#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        client.entities.ColumnTypes.models
# Purpose:     Creates a model, and pre-loads several publication types.  This
#              allows us to use a spreadsheet to load in a title list for a
#              database, either manually or automatically.
#
# Author:      sgallagherstarr
#
# Created:     03/08/2012
# Copyright:   (c) sgallagherstarr 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from google.appengine.ext import ndb

from client.entities.VendorInfo.models import VendorInfo

# a basic list of column types and their descriptive labels in title list
# spreadsheets from several vendors.

# The dictionary key below corresponds to a property named in a TitleRecord.
initial_columns_data = {
  'source_type': { 'display_label': 'Source type',
          'vendor_labels': {
                             "EBSCOhost": "Source Type",
                             "Gale/Cengage": "Format",
                           }
        },
  'standard_number': { 'display_label': 'Standard number',
          'vendor_labels': {
                             "EBSCOhost": [ "ISSN", "ISSN / ISBN", ],
                             "Gale/Cengage": "ISSN",
                           }
        },
  'publication_name': { 'display_label': 'Publication name',
          'vendor_labels': {
                             "EBSCOhost": "Publication name",
                             "Gale/Cengage": "Journal name",
                           }
        },
  'publisher': { 'display_label': "Publisher",
          'vendor_labels': {
                             "EBSCOhost": "Publisher",
                             "Gale/Cengage": "Publisher Name",
                           }
        },
  'indexing_start': { 'display_label': "Indexing and abstracting start",
          'vendor_labels': {
                             "EBSCOhost": "Indexing and Abstracting Start",
                             "Gale/Cengage": "Index Start",
                           }
        },
  'indexing_end': { 'display_label': "Indexing and abstracting end",
          'vendor_labels': {
                             "EBSCOhost": "Indexing and Abstracting Stop",
                             "Gale/Cengage": "Index End",
                           }
        },
  'fulltext_start': { 'display_label': "Full-text start",
          'vendor_labels': {
                             "EBSCOhost": "Full Text Start",
                             "Gale/Cengage": "Full-text Start",
                           }
        },
  'fulltext_end': { 'display_label': "Full-text stop",
          'vendor_labels': {
                             "EBSCOhost": "Full Text Stop",
                             "Gale/Cengage": "Full-text End",
                           }
        },
  'embargo': { 'display_label': 'Embargo period',
          'vendor_labels': {
                             "EBSCOhost": "Full Text Delay (Months)",
                             "Gale/Cengage": "Embargo (Days)",
                           }
        },
  'peer_reviewed': { 'display_label': "Peer-Reviewed",
          'vendor_labels': {
                             "EBSCOhost": "Peer-Reviewed",
                             "Gale/Cengage": "Refereed/Peer-Reviewed",
                           }
        },
  'availability': { 'display_label': "Availability",
          'vendor_labels': {
                             "EBSCOhost": "Availability*",
                             "Gale/Cengage": "Availability",
                           }
        },
  'pdf_images': { 'display_label': "PDF Images (full page)",
          'vendor_labels': {
                             "EBSCOhost": "PDF Images (full page)",
##                             "Gale/Cengage": "Format",
                           }
        },
  'image_quickview': { 'display_label': "Image QuickView",
          'vendor_labels': {
                             "EBSCOhost": "Image QuickView",
##                             "Gale/Cengage": "Format",
                           }
        },
  'searchable_cited_start': { 'display_label': "Searchable Cited References Start",
          'vendor_labels': {
                             "EBSCOhost": "Searchable Cited References Start",
##                             "Gale/Cengage": "Format",
                           }
        },
  'searchable_cited_end': { 'display_label': "Searchable Cited References Stop",
          'vendor_labels': {
                             "EBSCOhost": "Searchable Cited References Stop",
##                             "Gale/Cengage": "Format",
                           }
        },
  'image_start': { 'display_label': "Image Start",
          'vendor_labels': {
##                             "EBSCOhost": "Searchable Cited References Stop",
                             "Gale/Cengage": "Image Start",
                           }
        },
  'image_end': { 'display_label': "Image End",
          'vendor_labels': {
##                             "EBSCOhost": "Searchable Cited References Stop",
                             "Gale/Cengage": "Image End",
                           }
        },
  'publisher_country': { 'display_label': "Publisher Country",
          'vendor_labels': {
##                             "EBSCOhost": "Searchable Cited References Stop",
                             "Gale/Cengage": "Publisher Country",
                           }
        },
  'language': { 'display_label': "Language",
          'vendor_labels': {
##                             "EBSCOhost": "Searchable Cited References Stop",
                             "Gale/Cengage": "Language",
                           }
        },
  'primary_subject': { 'display_label': "Publication Primary Subject",
          'vendor_labels': {
##                             "EBSCOhost": "Searchable Cited References Stop",
                             "Gale/Cengage": "Publication Primary Subject",
                           }
        },
  'coverage_policy': { 'display_label': "Coverage Policy",
          'vendor_labels': {
                             "EBSCOhost": "Coverage Policy",
##                             "Gale/Cengage": "Format",
                           }
        },
}


class VendorLabels(ndb.Model):
  """Each vendor may have multiple labels for a type of column, depending on the
     source spreadsheet.  This gives us a way to list all of the alternatives.
  """
  vendor = ndb.KeyProperty(VendorInfo, indexed=True)
  column_labels = ndb.StringProperty(indexed=True, repeated=True)


class ColumnTypes(ndb.Model):
  display_label = ndb.StringProperty(indexed=True)
  column_reference = ndb.StringProperty(indexed=True)

  labels = ndb.StructuredProperty(VendorLabels, repeated=True)
