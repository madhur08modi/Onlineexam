# -*- coding: utf-8 -*-
db.define_table('ques',Field('comments','text',requires=IS_NOT_EMPTY()),auth.signature)
