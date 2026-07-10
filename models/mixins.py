"""اینترفیس‌های Rentable و Insurable به‌صورت Mixin.

هر Mixin یک قابلیت مستقل را اضافه می‌کند. کلاس‌های فرزند فقط در صورت
نیاز از آن‌ها ارث‌بری می‌کنند (اصل Interface Segregation).
"""

from abc import abstractmethod


class Rentable:
    """قابلیت اجاره‌دهی.

    کلاس‌هایی که این Mixin را می‌گیرند باید ``daily_rental_rate`` را
    پیاده‌سازی کنند؛ منطق محاسبهٔ هزینه (شامل تخفیف) اینجا مشترک است.
    """

    LONG_TERM_DAYS = 7
    LONG_TERM_DISCOUNT = 0.10  # ۱۰٪ تخفیف برای اجاره‌های یک‌هفته‌ای و بیشتر

    @abstractmethod
    def daily_rental_rate(self) -> float:
        """نرخ اجارهٔ روزانه؛ هر وسیله مقدار خود را برمی‌گرداند."""

    def calculate_rental_cost(self, days: int) -> float:
        if days <= 0:
            raise ValueError("تعداد روز اجاره باید مثبت باشد")
        cost = self.daily_rental_rate() * days
        if days >= self.LONG_TERM_DAYS:
            cost *= (1 - self.LONG_TERM_DISCOUNT)
        return cost


class Insurable:
    """قابلیت بیمه‌شدن.

    هزینهٔ بیمه بر پایهٔ ``base_price`` (از کلاس ``Vehicle``) و یک
    ضریب ریسک مخصوص هر وسیله محاسبه می‌شود.
    """

    BASE_INSURANCE_RATE = 0.05  # ۵٪ نرخ پایهٔ بیمهٔ سالانه

    @abstractmethod
    def risk_factor(self) -> float:
        """ضریب ریسک؛ هرچه بالاتر باشد بیمه گران‌تر است."""

    def calculate_insurance(self) -> float:
        return self.base_price * self.BASE_INSURANCE_RATE * self.risk_factor()
