# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'focusapp_person', (
            ('kbid', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('pic', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'focusapp', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'focusapp_person')


    models = {
        u'focusapp.person': {
            'Meta': {'object_name': 'Person'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'kbid': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pic': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['focusapp']