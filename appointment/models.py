# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Ticket(models.Model):
    game = models.IntegerField(default=1)
    time = models.CharField(max_length=11)
    number = models.IntegerField(default=6)

    def __unicode__(self):
        return u'%s, %s' % (self.game, self.time)

class User(models.Model):
    username = models.CharField(max_length=200)
    thu_id = models.CharField(max_length=10)
    tel = models.CharField(max_length=11)
    ticket = models.ForeignKey(Ticket)

    def __unicode__(self):
        if self.ticket.game == 1:
            gamename = u'撕名牌'
        else:
            gamename = u'泡泡足球'
        return u'%s, %s, %s, %s, %s' % (self.username, self.thu_id, self.tel, gamename, self.ticket.time)

