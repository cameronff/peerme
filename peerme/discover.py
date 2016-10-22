#!/usr/bin/env python3

'''
    Class to take care of discovering potential peers
'''

#import asyncio
import click
import logging

# TODO(cooper): Make relative imports work
#from . import peerme
from peerme import PeermeCmd


class DiscoverCli():

    @click.command()
    @click.option(
        '-y',
        '--yes',
        help='Auto confirm ...',
        is_flag=True,
    )
    @click.pass_obj
    def discover(cli_opts, yes):
        ''' All Discovered potential peerings '''
        DiscoverPeers(cli_opts).run(yes)


class DiscoverPeers(PeermeCmd):

    # TODO: Delete
    async def dbTest(self):
        sql_data = await self.opts.db.execute_query()
        print("GOT '{}' from DB".format(sql_data))

    def run(self, yes):
        click.echo("Time to get some peers discovered - Debug = {}".format(
            self.opts.debug
        ))

        click.echo("Config {} = {}".format(self.opts.config.conf_file,
                                           self.opts.config))

        # DB Connection Pool
#        self.opts.loop.run_until_complete(self.dbTest())  # DEBUG