import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    console.log('log');
    console.error('error');
    console.warn('warn');
    console.debug('debug');
    console.info('info');
    return 'Hello World!';
  }
}
