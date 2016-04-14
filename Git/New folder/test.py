def _get_total(self, cr, uid, ids, name, args, context=None):
        res = []
        total=0
        for rec in self.browse(cr, uid, ids):
            for total in rec.discount_ids:
                count_ob = total.amount
                total=total+(count_ob)
                print total
        res[rec.id] = total
        return res