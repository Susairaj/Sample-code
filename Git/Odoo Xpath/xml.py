Xpath in tree::
<xpath expr="//tree[@string='Attachments']" position="attributes">
	<attribute name="colors">orange:state=='request_review';green:type == 'binary'; blue:type =='url';</attribute>
</xpath>

lable and placeholder::

<label for="description" string="Description"/>
<field name="description" nolabel='1' placeholder='Description'/>

How to use option::

options="{'no_create': True, 'no_open': True}"

Create write one2many fields:::
(0, 0,  { values })    link to a new record that needs to be created with the given values dictionary
(1, ID, { values })    update the linked record with id = ID (write *values* on it)
(2, ID)                remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)
(3, ID)                cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)
(4, ID)                link to existing record with id = ID (adds a relationship)
(5)                    unlink all (like using (3,ID) for all linked records)
(6, 0, [IDs])          replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
###


Try this Values, If the second.class obj has partner than one2many is created.

obj = self.browse(cr, uid, ids)[0]

if obj.partner_id:
    vals{
    'partner_id': obj.partner_id.id,
    'res_ids': [(0,0, {
                    'partner_id': obj.partner_id.id,   #give id of partner 
                    'first_id': obj.first_id.id   #give id of first
             })]
    }
    self.pool.get('first.class').create(cr, uid, vals)

##########
Create , write many2many fields:::

    For Many2many

    For a many2many field, a list of tuples is expected. Here is the list of tuple that are accepted, with the corresponding semantics

    (0, 0, { values }) link to a new record that needs to be created with the given values dictionary

    (1, ID, { values }) update the linked record with id = ID (write values on it)

    (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

    (3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)

    (4, ID) link to existing record with id = ID (adds a relationship)

    (5) unlink all (like using (3,ID) for all linked records)

    (6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

    Example: [(6, 0, [8, 5, 6, 4])] sets the many2many to ids [8, 5, 6, 4]

    And One2many :

    (0, 0, { values }) link to a new record that needs to be created with the given values dictionary

    (1, ID, { values }) update the linked record with id = ID (write values on it)

    (2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

    Example: [(0, 0, {'field_name':field_value_record1, ...}), (0, 0, {'field_name':field_value_record2, ...})]

