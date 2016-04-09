# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RouteItem.code_prefix'
        db.add_column(u'maps_routeitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'SegmentSubItem.code_prefix'
        db.add_column(u'maps_segmentsubitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'CrossingSubItem.code_prefix'
        db.add_column(u'maps_crossingsubitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'CuldesacSubItem.code_prefix'
        db.add_column(u'maps_culdesacsubitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'RouteSubItem.code_prefix'
        db.add_column(u'maps_routesubitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'CrossingItem.code_prefix'
        db.add_column(u'maps_crossingitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'CuldesacItem.code_prefix'
        db.add_column(u'maps_culdesacitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)

        # Adding field 'SegmentItem.code_prefix'
        db.add_column(u'maps_segmentitem', 'code_prefix',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['maps.CodePrefix']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RouteItem.code_prefix'
        db.delete_column(u'maps_routeitem', 'code_prefix_id')

        # Deleting field 'SegmentSubItem.code_prefix'
        db.delete_column(u'maps_segmentsubitem', 'code_prefix_id')

        # Deleting field 'CrossingSubItem.code_prefix'
        db.delete_column(u'maps_crossingsubitem', 'code_prefix_id')

        # Deleting field 'CuldesacSubItem.code_prefix'
        db.delete_column(u'maps_culdesacsubitem', 'code_prefix_id')

        # Deleting field 'RouteSubItem.code_prefix'
        db.delete_column(u'maps_routesubitem', 'code_prefix_id')

        # Deleting field 'CrossingItem.code_prefix'
        db.delete_column(u'maps_crossingitem', 'code_prefix_id')

        # Deleting field 'CuldesacItem.code_prefix'
        db.delete_column(u'maps_culdesacitem', 'code_prefix_id')

        # Deleting field 'SegmentItem.code_prefix'
        db.delete_column(u'maps_segmentitem', 'code_prefix_id')


    models = {
        u'maps.codeprefix': {
            'Meta': {'object_name': 'CodePrefix'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.crossingitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CrossingItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CrossingItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.crossingsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CrossingSubItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CrossingSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.culdesacitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CuldesacItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CuldesacItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.culdesacsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CuldesacSubItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.CuldesacSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.routeitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'RouteItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.RouteItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.routesubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'RouteSubItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.RouteSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.segmentitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'SegmentItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.SegmentItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.segmentsubitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'SegmentSubItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'code_prefix': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['maps.CodePrefix']"}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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