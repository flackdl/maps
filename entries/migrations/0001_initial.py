# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntryLog'
        db.create_table(u'entries_entrylog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('survey_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('json', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'entries', ['EntryLog'])

        # Adding model 'EntryLogMessage'
        db.create_table(u'entries_entrylogmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_log', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryLog'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'entries', ['EntryLogMessage'])

        # Adding model 'Entry'
        db.create_table(u'entries_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Survey'])),
            ('auditor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('route_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('submitted', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'entries', ['Entry'])

        # Adding model 'EntryRouteSection'
        db.create_table(u'entries_entryroutesection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.Entry'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteSection'])

        # Adding model 'EntryRouteItemOption'
        db.create_table(u'entries_entryrouteitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteItemOption'])

        # Adding model 'EntryRouteSubItemOption'
        db.create_table(u'entries_entryroutesubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteSubItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteSubItemOption'])

        # Adding model 'EntryRouteItemAuxiliary'
        db.create_table(u'entries_entryrouteitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteItemAuxiliary'])

        # Adding model 'EntryRouteSubItemAuxiliary'
        db.create_table(u'entries_entryroutesubitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteSubItemAuxiliary'])

        # Adding model 'EntryRouteItemNA'
        db.create_table(u'entries_entryrouteitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteItemNA'])

        # Adding model 'EntryRouteSubItemNA'
        db.create_table(u'entries_entryroutesubitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryRouteSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.RouteSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryRouteSubItemNA'])

        # Adding model 'EntrySegmentSection'
        db.create_table(u'entries_entrysegmentsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.Entry'])),
            ('segment_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('starting_xstreet', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('ending_xstreet', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentSection'])

        # Adding model 'EntrySegmentItemOption'
        db.create_table(u'entries_entrysegmentitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentItemOption'])

        # Adding model 'EntrySegmentSubItemOption'
        db.create_table(u'entries_entrysegmentsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentSubItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentSubItemOption'])

        # Adding model 'EntrySegmentItemAuxiliary'
        db.create_table(u'entries_entrysegmentitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentItem'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentItemAuxiliary'])

        # Adding model 'EntrySegmentSubItemAuxiliary'
        db.create_table(u'entries_entrysegmentsubitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentSubItemAuxiliary'])

        # Adding model 'EntrySegmentItemNA'
        db.create_table(u'entries_entrysegmentitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentItem'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentItemNA'])

        # Adding model 'EntrySegmentSubItemNA'
        db.create_table(u'entries_entrysegmentsubitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntrySegmentSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.SegmentSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntrySegmentSubItemNA'])

        # Adding model 'EntryCrossingSection'
        db.create_table(u'entries_entrycrossingsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.Entry'])),
            ('crossing_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('crossing_from', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('crossing_to', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('intersection1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('intersection2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingSection'])

        # Adding model 'EntryCrossingItemOption'
        db.create_table(u'entries_entrycrossingitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingItemOption'])

        # Adding model 'EntryCrossingSubItemOption'
        db.create_table(u'entries_entrycrossingsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingSubItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingSubItemOption'])

        # Adding model 'EntryCrossingItemAuxiliary'
        db.create_table(u'entries_entrycrossingitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingItemAuxiliary'])

        # Adding model 'EntryCrossingSubItemAuxiliary'
        db.create_table(u'entries_entrycrossingsubitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingSubItemAuxiliary'])

        # Adding model 'EntryCrossingItemNA'
        db.create_table(u'entries_entrycrossingitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingItemNA'])

        # Adding model 'EntryCrossingSubItemNA'
        db.create_table(u'entries_entrycrossingsubitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CrossingSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCrossingSubItemNA'])

        # Adding model 'EntryCuldesacSection'
        db.create_table(u'entries_entryculdesacsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.Entry'])),
            ('culdesac_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacSection'])

        # Adding model 'EntryCuldesacItemOption'
        db.create_table(u'entries_entryculdesacitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCuldesacSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacItemOption'])

        # Adding model 'EntryCuldesacSubItemOption'
        db.create_table(u'entries_entryculdesacsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCuldesacSection'])),
            ('option', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacSubItemOption'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacSubItemOption'])

        # Adding model 'EntryCuldesacItemAuxiliary'
        db.create_table(u'entries_entryculdesacitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCuldesacSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacItemAuxiliary'])

        # Adding model 'EntryCuldesacSubItemAuxiliary'
        db.create_table(u'entries_entryculdesacsubitemauxiliary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCuldesacSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacSubItemAuxiliary'])

        # Adding model 'EntryCuldesacItemNA'
        db.create_table(u'entries_entryculdesacitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacItemNA'])

        # Adding model 'EntryCuldesacSubItemNA'
        db.create_table(u'entries_entryculdesacsubitemna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['entries.EntryCrossingSection'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.CuldesacSubItem'])),
        ))
        db.send_create_signal(u'entries', ['EntryCuldesacSubItemNA'])


    def backwards(self, orm):
        # Deleting model 'EntryLog'
        db.delete_table(u'entries_entrylog')

        # Deleting model 'EntryLogMessage'
        db.delete_table(u'entries_entrylogmessage')

        # Deleting model 'Entry'
        db.delete_table(u'entries_entry')

        # Deleting model 'EntryRouteSection'
        db.delete_table(u'entries_entryroutesection')

        # Deleting model 'EntryRouteItemOption'
        db.delete_table(u'entries_entryrouteitemoption')

        # Deleting model 'EntryRouteSubItemOption'
        db.delete_table(u'entries_entryroutesubitemoption')

        # Deleting model 'EntryRouteItemAuxiliary'
        db.delete_table(u'entries_entryrouteitemauxiliary')

        # Deleting model 'EntryRouteSubItemAuxiliary'
        db.delete_table(u'entries_entryroutesubitemauxiliary')

        # Deleting model 'EntryRouteItemNA'
        db.delete_table(u'entries_entryrouteitemna')

        # Deleting model 'EntryRouteSubItemNA'
        db.delete_table(u'entries_entryroutesubitemna')

        # Deleting model 'EntrySegmentSection'
        db.delete_table(u'entries_entrysegmentsection')

        # Deleting model 'EntrySegmentItemOption'
        db.delete_table(u'entries_entrysegmentitemoption')

        # Deleting model 'EntrySegmentSubItemOption'
        db.delete_table(u'entries_entrysegmentsubitemoption')

        # Deleting model 'EntrySegmentItemAuxiliary'
        db.delete_table(u'entries_entrysegmentitemauxiliary')

        # Deleting model 'EntrySegmentSubItemAuxiliary'
        db.delete_table(u'entries_entrysegmentsubitemauxiliary')

        # Deleting model 'EntrySegmentItemNA'
        db.delete_table(u'entries_entrysegmentitemna')

        # Deleting model 'EntrySegmentSubItemNA'
        db.delete_table(u'entries_entrysegmentsubitemna')

        # Deleting model 'EntryCrossingSection'
        db.delete_table(u'entries_entrycrossingsection')

        # Deleting model 'EntryCrossingItemOption'
        db.delete_table(u'entries_entrycrossingitemoption')

        # Deleting model 'EntryCrossingSubItemOption'
        db.delete_table(u'entries_entrycrossingsubitemoption')

        # Deleting model 'EntryCrossingItemAuxiliary'
        db.delete_table(u'entries_entrycrossingitemauxiliary')

        # Deleting model 'EntryCrossingSubItemAuxiliary'
        db.delete_table(u'entries_entrycrossingsubitemauxiliary')

        # Deleting model 'EntryCrossingItemNA'
        db.delete_table(u'entries_entrycrossingitemna')

        # Deleting model 'EntryCrossingSubItemNA'
        db.delete_table(u'entries_entrycrossingsubitemna')

        # Deleting model 'EntryCuldesacSection'
        db.delete_table(u'entries_entryculdesacsection')

        # Deleting model 'EntryCuldesacItemOption'
        db.delete_table(u'entries_entryculdesacitemoption')

        # Deleting model 'EntryCuldesacSubItemOption'
        db.delete_table(u'entries_entryculdesacsubitemoption')

        # Deleting model 'EntryCuldesacItemAuxiliary'
        db.delete_table(u'entries_entryculdesacitemauxiliary')

        # Deleting model 'EntryCuldesacSubItemAuxiliary'
        db.delete_table(u'entries_entryculdesacsubitemauxiliary')

        # Deleting model 'EntryCuldesacItemNA'
        db.delete_table(u'entries_entryculdesacitemna')

        # Deleting model 'EntryCuldesacSubItemNA'
        db.delete_table(u'entries_entryculdesacsubitemna')


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
            'end_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
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
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['entries']