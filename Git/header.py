<header>
							<field name="is_current_user" invisible="1" />
							<field name="is_executive_group" invisible="1" />
							<field name="is_system_admin_group" invisible="1" />
							<field name="is_user_group" invisible="1" />
							<field name="issue_stage_name" invisible="1" />
							<button name="act_move_stage" string="Acknowledged" type="object"
								class="oe_highlight" context="{'move_stage': 'Acknowledged' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Identified'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Analysis" type="object"
								class="oe_highlight" context="{'move_stage': 'Analysis' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Acknowledged'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Solution" type="object"
								class="oe_highlight" context="{'move_stage': 'Solution' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Analysis'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Development" type="object"
								class="oe_highlight" context="{'move_stage': 'Development' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Solution'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Internal Sign off"
								type="object" class="oe_highlight" context="{'move_stage': 'Internal Sign off' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Development'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Client Sign off"
								type="object" class="oe_highlight" context="{'move_stage': 'Client Sign off' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Internal Sign off'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<button name="act_move_stage" string="Production" type="object"
								class="oe_highlight" context="{'move_stage': 'Production' }"
								attrs="{'invisible':['|','&amp;', ('issue_stage_name','!=', 'Client Sign off'), ('is_current_user','=',False), ('is_system_admin_group','=',False)]}" />
							<field name="issue_stage_id" widget="statusbar"
								options="{'fold_field': 'fold'}" />
						</header>