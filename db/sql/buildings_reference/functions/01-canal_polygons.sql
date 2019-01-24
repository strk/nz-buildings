--------------------------------------------
-- buildings_reference.canal_polygons

-- Functions

-- canal_polygons_delete_by_external_id
    -- params: integer external_canal_polygon_id
    -- return: integer canal_polygon_id

-- canal_polygons_insert
    -- params: integer external_canal_polygon_id, varchar geometry
    -- return: integer canal_polygon_id


--------------------------------------------

-- Functions

-- canal_polygons_delete_by_external_id ()
    -- params: integer external_canal_polygon_id
    -- return: integer canal_polygon_id

CREATE OR REPLACE FUNCTION buildings_reference.canal_polygons_delete_by_external_id(integer)
RETURNS integer AS
$$
    DELETE FROM buildings_reference.canal_polygons
    WHERE external_canal_polygon_id = $1
    RETURNING canal_polygon_id;

$$
LANGUAGE sql VOLATILE;

COMMENT ON FUNCTION buildings_reference.canal_polygons_delete_by_external_id(integer) IS
'Delete from canal polygons table by external id';


-- canal_polygons_insert
    -- params: integer external_canal_polygon_id, varchar geometry
    -- return: integer canal_polygon_id

CREATE OR REPLACE FUNCTION buildings_reference.canal_polygons_insert(integer, varchar)
RETURNS integer AS
$$
    INSERT INTO buildings_reference.canal_polygons (external_canal_polygon_id, shape)
    VALUES ($1, ST_SetSRID(ST_GeometryFromText($2), 2193))
    RETURNING canal_polygon_id;

$$
LANGUAGE sql VOLATILE;

COMMENT ON FUNCTION buildings_reference.canal_polygons_insert(integer, varchar) IS
'Insert new entry into canal polygons table';


-- canal_polygons_update_shape_by_external_id
    -- params: integer external_canal_polygon_id, varchar geometry
    -- return: integer canal_polygon_id

CREATE OR REPLACE FUNCTION buildings_reference.canal_polygons_update_shape_by_external_id(integer, varchar)
RETURNS integer AS
$$
    UPDATE buildings_reference.canal_polygons
    SET shape = ST_SetSRID(ST_GeometryFromText($2), 2193)
    WHERE external_canal_polygon_id = $1
    RETURNING canal_polygon_id;

$$
LANGUAGE sql VOLATILE;

COMMENT ON FUNCTION buildings_reference.canal_polygons_update_shape_by_external_id(integer, varchar) IS
'Update geometry of canal based on external_river_polygon_id';
