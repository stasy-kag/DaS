import sys
from analytics import Research, Analytics
import config


if __name__ == "__main__":
    try:
        obj = Research(sys.argv[1])
        data = obj.file_reader()

        calc = obj.Calculations(data)
        heads, tails = calc.counts()
        frac_heads, frac_tails = calc.fractions(heads, tails)

        analytic = Analytics(data)
        predict = analytic.predict_random(config.num_of_steps)

        pred_tail = sum(1 for p in predict if p[0] == 1)
        pred_head = len(predict) - pred_tail

        report = config.report.format(
            total=heads + tails,
            heads=heads,
            tails=tails,
            frac_heads=frac_heads,
            frac_tails=frac_tails,
            pred_head=pred_head,
            pred_tail=pred_tail,
        )

        analytic.save_file(report, config.output, config.extension)
        obj.send_message(config.telegram_webhook, "Отчёт успешно создан")

    except Exception as e:
        err_msg = f"Отчёт не создан из-за ошибки: {e}"
        print(err_msg)
        try:
            obj.send_message(config.telegram_webhook, err_msg)
        except Exception:
            pass
        raise
