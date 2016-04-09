# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RouteItem.code'
        db.delete_column(u'maps_routeitem', 'code')

        # Deleting field 'SegmentItemOption.code'
        db.delete_column(u'maps_segmentitemoption', 'code')

        # Deleting field 'SegmentSubItem.code'
        db.delete_column(u'maps_segmentsubitem', 'code')

        # Deleting field 'CuldesacSubItemOption.code'
        db.delete_column(u'maps_culdesacsubitemoption', 'code')

        # Deleting field 'CrossingSubItem.code'
        db.delete_column(u'maps_crossingsubitem', 'code')

        # Deleting field 'CuldesacSubItem.code'
        db.delete_column(u'maps_culdesacsubitem', 'code')

        # Deleting field 'RouteSubItem.code'
        db.delete_column(u'maps_routesubitem', 'code')

        # Deleting field 'RouteItemOption.code'
        db.delete_column(u'maps_routeitemoption', 'code')

        # Deleting field 'CuldesacItemOption.code'
        db.delete_column(u'maps_culdesacitemoption', 'code')

        # Deleting field 'CrossingItem.code'
        db.delete_column(u'maps_crossingitem', 'code')

        # Deleting field 'CrossingItemOption.code'
        db.delete_column(u'maps_crossingitemoption', 'code')

        # Deleting field 'CuldesacItem.code'
        db.delete_column(u'maps_culdesacitem', 'code')

        # Deleting field 'RouteSubItemOption.code'
        db.delete_column(u'maps_routesubitemoption', 'code')

        # Deleting field 'SegmentItem.code'
        db.delete_column(u'maps_segmentitem', 'code')

        # Deleting field 'CrossingSubItemOption.code'
        db.delete_column(u'maps_crossingsubitemoption', 'code')

        # Deleting field 'SegmentSubItemOption.code'
        db.delete_column(u'maps_segmentsubitemoption', 'code')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'RouteItem.code'
        raise RuntimeError("Cannot reverse this migration. 'RouteItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RouteItem.code'
        db.add_column(u'maps_routeitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SegmentItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'SegmentItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SegmentItemOption.code'
        db.add_column(u'maps_segmentitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SegmentSubItem.code'
        raise RuntimeError("Cannot reverse this migration. 'SegmentSubItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SegmentSubItem.code'
        db.add_column(u'maps_segmentsubitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CuldesacSubItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'CuldesacSubItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CuldesacSubItemOption.code'
        db.add_column(u'maps_culdesacsubitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CrossingSubItem.code'
        raise RuntimeError("Cannot reverse this migration. 'CrossingSubItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CrossingSubItem.code'
        db.add_column(u'maps_crossingsubitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CuldesacSubItem.code'
        raise RuntimeError("Cannot reverse this migration. 'CuldesacSubItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CuldesacSubItem.code'
        db.add_column(u'maps_culdesacsubitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'RouteSubItem.code'
        raise RuntimeError("Cannot reverse this migration. 'RouteSubItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RouteSubItem.code'
        db.add_column(u'maps_routesubitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'RouteItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'RouteItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RouteItemOption.code'
        db.add_column(u'maps_routeitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CuldesacItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'CuldesacItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CuldesacItemOption.code'
        db.add_column(u'maps_culdesacitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CrossingItem.code'
        raise RuntimeError("Cannot reverse this migration. 'CrossingItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CrossingItem.code'
        db.add_column(u'maps_crossingitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CrossingItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'CrossingItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CrossingItemOption.code'
        db.add_column(u'maps_crossingitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CuldesacItem.code'
        raise RuntimeError("Cannot reverse this migration. 'CuldesacItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CuldesacItem.code'
        db.add_column(u'maps_culdesacitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'RouteSubItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'RouteSubItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RouteSubItemOption.code'
        db.add_column(u'maps_routesubitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SegmentItem.code'
        raise RuntimeError("Cannot reverse this migration. 'SegmentItem.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SegmentItem.code'
        db.add_column(u'maps_segmentitem', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CrossingSubItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'CrossingSubItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CrossingSubItemOption.code'
        db.add_column(u'maps_crossingsubitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SegmentSubItemOption.code'
        raise RuntimeError("Cannot reverse this migration. 'SegmentSubItemOption.code' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SegmentSubItemOption.code'
        db.add_column(u'maps_segmentsubitemoption', 'code',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


    models = {
        u'maps.codeprefix': {
            'Meta': {'object_name': 'CodePrefix'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.crossingitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CrossingItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.Survey']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.crossingitemhelper': {
            'Meta': {'object_name': 'CrossingItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.CrossingItem']"})
        },
        u'maps.crossingitemoption': {
            'Meta': {'object_name': 'CrossingItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CrossingItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.crossingsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CrossingSubItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subitem_set'", 'to': u"orm['maps.CrossingItem']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.crossingsubitemhelper': {
            'Meta': {'object_name': 'CrossingSubItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.CrossingSubItem']"})
        },
        u'maps.crossingsubitemoption': {
            'Meta': {'object_name': 'CrossingSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CrossingSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.culdesacitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CuldesacItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.Survey']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.culdesacitemhelper': {
            'Meta': {'object_name': 'CuldesacItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.CuldesacItem']"})
        },
        u'maps.culdesacitemoption': {
            'Meta': {'object_name': 'CuldesacItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CuldesacItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.culdesacsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CuldesacSubItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subitem_set'", 'to': u"orm['maps.CuldesacItem']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.culdesacsubitemhelper': {
            'Meta': {'object_name': 'CuldesacSubItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.CuldesacSubItem']"})
        },
        u'maps.culdesacsubitemoption': {
            'Meta': {'object_name': 'CuldesacSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CuldesacSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.routeitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'RouteItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.Survey']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.routeitemhelper': {
            'Meta': {'object_name': 'RouteItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.RouteItem']"})
        },
        u'maps.routeitemoption': {
            'Meta': {'object_name': 'RouteItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.RouteItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.routesubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'RouteSubItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subitem_set'", 'to': u"orm['maps.RouteItem']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.routesubitemhelper': {
            'Meta': {'object_name': 'RouteSubItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.RouteSubItem']"})
        },
        u'maps.routesubitemoption': {
            'Meta': {'object_name': 'RouteSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.RouteSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.segmentitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'SegmentItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.Survey']"}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.segmentitemhelper': {
            'Meta': {'object_name': 'SegmentItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.SegmentItem']"})
        },
        u'maps.segmentitemoption': {
            'Meta': {'object_name': 'SegmentItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.SegmentItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.segmentsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'SegmentSubItem'},
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CodePrefix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_not_applicable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subitem_set'", 'to': u"orm['maps.SegmentItem']"}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'maps.segmentsubitemhelper': {
            'Meta': {'object_name': 'SegmentSubItemHelper'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemhelper_set'", 'to': u"orm['maps.SegmentSubItem']"})
        },
        u'maps.segmentsubitemoption': {
            'Meta': {'object_name': 'SegmentSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.SegmentSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['maps']