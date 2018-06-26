# -*- coding: utf-8 -*-
"""
################################################################################
#
# Copyright 2018 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the 3 clause BSD license. See the
# LICENSE file for more information.
#
################################################################################

    Tests: Compare Outlines Button Click Confirm Processes

 ***************************************************************************/
"""

import unittest

from qgis.utils import plugins

from buildings.utilities import database as db


class SetUpEditBulkLoad(unittest.TestCase):
    """
    Test Add Production Outline GUI initial
    setup confirm default settings
    """
    @classmethod
    def setUpClass(cls):
        """Runs at TestCase init."""
        if not plugins.get('roads'):
            pass
        else:
            cls.road_plugin = plugins.get('roads')
            if cls.road_plugin.is_active is False:
                cls.road_plugin.main_toolbar.actions()[0].trigger()
                cls.dockwidget = cls.road_plugin.dockwidget
            else:
                cls.dockwidget = cls.road_plugin.dockwidget
            if not plugins.get('buildings'):
                pass
            else:
                cls.building_plugin = plugins.get('buildings')
                cls.building_plugin.main_toolbar.actions()[0].trigger()

    @classmethod
    def tearDownClass(cls):
        """Runs at TestCase teardown."""
        cls.road_plugin.dockwidget.close()

    def setUp(self):
        """Runs before each test."""
        self.road_plugin = plugins.get('roads')
        self.building_plugin = plugins.get('buildings')
        self.dockwidget = self.road_plugin.dockwidget
        self.startup_frame = self.building_plugin.startup_frame
        self.startup_frame.btn_bulk_load.click()
        self.bulk_load_frame = self.dockwidget.current_frame
        self.bulk_load_frame.db.open_cursor()
        self.bulk_load_frame.publish_clicked(False)

    def tearDown(self):
        """Runs after each test."""
        self.bulk_load_frame.btn_exit.click()

    def test_load_building_outlines(self):
        """"""
        sql = 'SELECT count(*) FROM buildings.building_outlines;'
        result = db._execute(sql)
        result = result.fetchall()
        self.assertEqual(result[0][0], 66)
        sql = 'SELECT count(*) FROM buildings.building_outlines WHERE end_lifespan IS NULL;'
        result = db._execute(sql)
        result = result.fetchall()
        self.assertEqual(result[0][0], 33)
        self.bulk_load_frame.db.rollback_open_cursor()

    def test_populate_building_lds(self):
        """"""
        sql = 'SELECT count(*) FROM buildings_lds.nz_building_outlines;'
        result = db._execute(sql)
        result = result.fetchall()
        self.assertEqual(result[0][0], 33)
        self.bulk_load_frame.db.rollback_open_cursor()

    def test_gui_on_publish_clicked(self):
        """"""
        self.assertEqual(self.bulk_load_frame.current_dataset, None)
        self.assertFalse(self.bulk_load_frame.btn_publish.isEnabled())
        self.assertFalse(self.bulk_load_frame.btn_compare_outlines.isEnabled())
        self.assertFalse(self.bulk_load_frame.btn_alter_rel.isEnabled())
        self.assertTrue(self.bulk_load_frame.ml_outlines_layer.isEnabled())
        self.assertTrue(self.bulk_load_frame.cmb_capture_method.isEnabled())
        self.assertTrue(self.bulk_load_frame.cmb_organisation.isEnabled())
        self.assertTrue(self.bulk_load_frame.cmb_capture_src_grp.isEnabled())
        self.assertTrue(self.bulk_load_frame.le_data_description.isEnabled())
        self.assertFalse(self.bulk_load_frame.rad_external_source.isChecked())
        self.assertFalse(self.bulk_load_frame.fcb_external_id.isEnabled())
        self.assertFalse(self.bulk_load_frame.cmb_external_id.isEnabled())
        self.bulk_load_frame.db.rollback_open_cursor()
