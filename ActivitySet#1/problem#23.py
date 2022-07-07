def test_respect_dtype_singleton(self):
        # See gh-7203
        for dt in self.itype:
            lbnd = 0 if dt is np.bool_ else np.iinfo(dt).min
            ubnd = 2 if dt is np.bool_ else np.iinfo(dt).max + 1

            sample = self.rfunc(lbnd, ubnd, dtype=dt)
            assert_equal(sample.dtype, np.dtype(dt))

        for dt in (bool, int, np.long):
            lbnd = 0 if dt is bool else np.iinfo(dt).min
            ubnd = 2 if dt is bool else np.iinfo(dt).max + 1

            # gh-7284: Ensure that we get Python data types
            sample = self.rfunc(lbnd, ubnd, dtype=dt)
            assert_(not hasattr(sample, 'dtype'))
            assert_equal(type(sample), dt) 