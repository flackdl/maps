# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'maps_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'maps', ['Survey'])

        # Adding model 'RouteItem'
        db.create_table(u'maps_routeitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Survey'])),
        ))
        db.send_create_signal(u'maps', ['RouteItem'])

        # Adding model 'RouteSubItem'
        db.create_table(u'maps_routesubitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subitem_set', to=orm['maps.RouteItem'])),
        ))
        db.send_create_signal(u'maps', ['RouteSubItem'])

        # Adding model 'SegmentItem'
        db.create_table(u'maps_segmentitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Survey'])),
        ))
        db.send_create_signal(u'maps', ['SegmentItem'])

        # Adding model 'SegmentSubItem'
        db.create_table(u'maps_segmentsubitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subitem_set', to=orm['maps.SegmentItem'])),
        ))
        db.send_create_signal(u'maps', ['SegmentSubItem'])

        # Adding model 'CrossingItem'
        db.create_table(u'maps_crossingitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Survey'])),
        ))
        db.send_create_signal(u'maps', ['CrossingItem'])

        # Adding model 'CrossingSubItem'
        db.create_table(u'maps_crossingsubitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subitem_set', to=orm['maps.CrossingItem'])),
        ))
        db.send_create_signal(u'maps', ['CrossingSubItem'])

        # Adding model 'CuldesacItem'
        db.create_table(u'maps_culdesacitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['maps.Survey'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacItem'])

        # Adding model 'CuldesacSubItem'
        db.create_table(u'maps_culdesacsubitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('include_not_applicable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subitem_set', to=orm['maps.CuldesacItem'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacSubItem'])

        # Adding model 'RouteItemOption'
        db.create_table(u'maps_routeitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.RouteItem'])),
        ))
        db.send_create_signal(u'maps', ['RouteItemOption'])

        # Adding model 'RouteSubItemOption'
        db.create_table(u'maps_routesubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.RouteSubItem'])),
        ))
        db.send_create_signal(u'maps', ['RouteSubItemOption'])

        # Adding model 'SegmentItemOption'
        db.create_table(u'maps_segmentitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.SegmentItem'])),
        ))
        db.send_create_signal(u'maps', ['SegmentItemOption'])

        # Adding model 'SegmentSubItemOption'
        db.create_table(u'maps_segmentsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.SegmentSubItem'])),
        ))
        db.send_create_signal(u'maps', ['SegmentSubItemOption'])

        # Adding model 'CrossingItemOption'
        db.create_table(u'maps_crossingitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.CrossingItem'])),
        ))
        db.send_create_signal(u'maps', ['CrossingItemOption'])

        # Adding model 'CrossingSubItemOption'
        db.create_table(u'maps_crossingsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.CrossingSubItem'])),
        ))
        db.send_create_signal(u'maps', ['CrossingSubItemOption'])

        # Adding model 'CuldesacItemOption'
        db.create_table(u'maps_culdesacitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.CuldesacItem'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacItemOption'])

        # Adding model 'CuldesacSubItemOption'
        db.create_table(u'maps_culdesacsubitemoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemoption_set', to=orm['maps.CuldesacSubItem'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacSubItemOption'])

        # Adding model 'RouteItemHelper'
        db.create_table(u'maps_routeitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.RouteItem'])),
        ))
        db.send_create_signal(u'maps', ['RouteItemHelper'])

        # Adding model 'RouteSubItemHelper'
        db.create_table(u'maps_routesubitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.RouteSubItem'])),
        ))
        db.send_create_signal(u'maps', ['RouteSubItemHelper'])

        # Adding model 'SegmentItemHelper'
        db.create_table(u'maps_segmentitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.SegmentItem'])),
        ))
        db.send_create_signal(u'maps', ['SegmentItemHelper'])

        # Adding model 'SegmentSubItemHelper'
        db.create_table(u'maps_segmentsubitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.SegmentSubItem'])),
        ))
        db.send_create_signal(u'maps', ['SegmentSubItemHelper'])

        # Adding model 'CrossingItemHelper'
        db.create_table(u'maps_crossingitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.CrossingItem'])),
        ))
        db.send_create_signal(u'maps', ['CrossingItemHelper'])

        # Adding model 'CrossingSubItemHelper'
        db.create_table(u'maps_crossingsubitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.CrossingSubItem'])),
        ))
        db.send_create_signal(u'maps', ['CrossingSubItemHelper'])

        # Adding model 'CuldesacItemHelper'
        db.create_table(u'maps_culdesacitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.CuldesacItem'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacItemHelper'])

        # Adding model 'CuldesacSubItemHelper'
        db.create_table(u'maps_culdesacsubitemhelper', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='itemhelper_set', to=orm['maps.CuldesacSubItem'])),
        ))
        db.send_create_signal(u'maps', ['CuldesacSubItemHelper'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table(u'maps_survey')

        # Deleting model 'RouteItem'
        db.delete_table(u'maps_routeitem')

        # Deleting model 'RouteSubItem'
        db.delete_table(u'maps_routesubitem')

        # Deleting model 'SegmentItem'
        db.delete_table(u'maps_segmentitem')

        # Deleting model 'SegmentSubItem'
        db.delete_table(u'maps_segmentsubitem')

        # Deleting model 'CrossingItem'
        db.delete_table(u'maps_crossingitem')

        # Deleting model 'CrossingSubItem'
        db.delete_table(u'maps_crossingsubitem')

        # Deleting model 'CuldesacItem'
        db.delete_table(u'maps_culdesacitem')

        # Deleting model 'CuldesacSubItem'
        db.delete_table(u'maps_culdesacsubitem')

        # Deleting model 'RouteItemOption'
        db.delete_table(u'maps_routeitemoption')

        # Deleting model 'RouteSubItemOption'
        db.delete_table(u'maps_routesubitemoption')

        # Deleting model 'SegmentItemOption'
        db.delete_table(u'maps_segmentitemoption')

        # Deleting model 'SegmentSubItemOption'
        db.delete_table(u'maps_segmentsubitemoption')

        # Deleting model 'CrossingItemOption'
        db.delete_table(u'maps_crossingitemoption')

        # Deleting model 'CrossingSubItemOption'
        db.delete_table(u'maps_crossingsubitemoption')

        # Deleting model 'CuldesacItemOption'
        db.delete_table(u'maps_culdesacitemoption')

        # Deleting model 'CuldesacSubItemOption'
        db.delete_table(u'maps_culdesacsubitemoption')

        # Deleting model 'RouteItemHelper'
        db.delete_table(u'maps_routeitemhelper')

        # Deleting model 'RouteSubItemHelper'
        db.delete_table(u'maps_routesubitemhelper')

        # Deleting model 'SegmentItemHelper'
        db.delete_table(u'maps_segmentitemhelper')

        # Deleting model 'SegmentSubItemHelper'
        db.delete_table(u'maps_segmentsubitemhelper')

        # Deleting model 'CrossingItemHelper'
        db.delete_table(u'maps_crossingitemhelper')

        # Deleting model 'CrossingSubItemHelper'
        db.delete_table(u'maps_crossingsubitemhelper')

        # Deleting model 'CuldesacItemHelper'
        db.delete_table(u'maps_culdesacitemhelper')

        # Deleting model 'CuldesacSubItemHelper'
        db.delete_table(u'maps_culdesacsubitemhelper')


    models = {
        u'maps.crossingitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CrossingItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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