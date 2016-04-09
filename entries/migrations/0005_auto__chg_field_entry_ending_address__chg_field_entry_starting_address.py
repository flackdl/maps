# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Entry.ending_address'
        db.alter_column(u'entries_entry', 'ending_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Entry.starting_address'
        db.alter_column(u'entries_entry', 'starting_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Entry.ending_address'
        db.alter_column(u'entries_entry', 'ending_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Entry.starting_address'
        db.alter_column(u'entries_entry', 'starting_address', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entries.entry': {
            'Meta': {'ordering': "('submitted',)", 'object_name': 'Entry'},
            'auditor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'ending_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'starting_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'submitted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.Survey']"})
        },
        u'entries.entrycrossingitemauxiliary': {
            'Meta': {'object_name': 'EntryCrossingItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entrycrossingitemna': {
            'Meta': {'object_name': 'EntryCrossingItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entrycrossingitemoption': {
            'Meta': {'object_name': 'EntryCrossingItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entrycrossingsection': {
            'Meta': {'object_name': 'EntryCrossingSection'},
            'crossing_from': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'crossing_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'crossing_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intersection1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'intersection2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'entries.entrycrossingsubitemauxiliary': {
            'Meta': {'object_name': 'EntryCrossingSubItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entrycrossingsubitemna': {
            'Meta': {'object_name': 'EntryCrossingSubItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entrycrossingsubitemoption': {
            'Meta': {'object_name': 'EntryCrossingSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CrossingSubItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entryculdesacitemauxiliary': {
            'Meta': {'object_name': 'EntryCuldesacItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCuldesacSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entryculdesacitemna': {
            'Meta': {'object_name': 'EntryCuldesacItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entryculdesacitemoption': {
            'Meta': {'object_name': 'EntryCuldesacItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCuldesacSection']"})
        },
        u'entries.entryculdesacsection': {
            'Meta': {'object_name': 'EntryCuldesacSection'},
            'culdesac_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'entries.entryculdesacsubitemauxiliary': {
            'Meta': {'object_name': 'EntryCuldesacSubItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCuldesacSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entryculdesacsubitemna': {
            'Meta': {'object_name': 'EntryCuldesacSubItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCrossingSection']"})
        },
        u'entries.entryculdesacsubitemoption': {
            'Meta': {'object_name': 'EntryCuldesacSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.CuldesacSubItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryCuldesacSection']"})
        },
        u'entries.entrylog': {
            'Meta': {'object_name': 'EntryLog'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'survey_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'entries.entrylogmessage': {
            'Meta': {'object_name': 'EntryLogMessage'},
            'entry_log': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryLog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'entries.entryrouteitemauxiliary': {
            'Meta': {'object_name': 'EntryRouteItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entryrouteitemna': {
            'Meta': {'object_name': 'EntryRouteItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"})
        },
        u'entries.entryrouteitemoption': {
            'Meta': {'object_name': 'EntryRouteItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"})
        },
        u'entries.entryroutesection': {
            'Meta': {'object_name': 'EntryRouteSection'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'entries.entryroutesubitemauxiliary': {
            'Meta': {'object_name': 'EntryRouteSubItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entryroutesubitemna': {
            'Meta': {'object_name': 'EntryRouteSubItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"})
        },
        u'entries.entryroutesubitemoption': {
            'Meta': {'object_name': 'EntryRouteSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.RouteSubItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntryRouteSection']"})
        },
        u'entries.entrysegmentitemauxiliary': {
            'Meta': {'object_name': 'EntrySegmentItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entrysegmentitemna': {
            'Meta': {'object_name': 'EntrySegmentItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"})
        },
        u'entries.entrysegmentitemoption': {
            'Meta': {'object_name': 'EntrySegmentItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"})
        },
        u'entries.entrysegmentsection': {
            'Meta': {'object_name': 'EntrySegmentSection'},
            'ending_xstreet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'segment_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'starting_xstreet': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'entries.entrysegmentsubitemauxiliary': {
            'Meta': {'object_name': 'EntrySegmentSubItemAuxiliary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'entries.entrysegmentsubitemna': {
            'Meta': {'object_name': 'EntrySegmentSubItemNA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentSubItem']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"})
        },
        u'entries.entrysegmentsubitemoption': {
            'Meta': {'object_name': 'EntrySegmentSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['maps.SegmentSubItemOption']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['entries.EntrySegmentSection']"})
        },
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.segmentsubitemoption': {
            'Meta': {'object_name': 'SegmentSubItemOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itemoption_set'", 'to': u"orm['maps.SegmentSubItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'maps.survey': {
            'Meta': {'ordering': "('id',)", 'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['entries']